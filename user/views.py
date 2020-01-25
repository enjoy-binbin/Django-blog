import logging
from random import Random

from django.contrib import messages
from django.contrib.auth import get_user_model, logout, login, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.shortcuts import reverse, redirect
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView, View

from user.forms import RegisterForm, LoginForm
from user.models import EmailVerifyCode
from user.tasks import send_email_task
from utils.get_setting import get_setting

User = get_user_model()
logger = logging.getLogger(__name__)


# django有一个 path('', include('django.contrib.auth.urls')),
# 有专门用于 登陆登出的View, 只是没有模板, 读一读里面的源码实现
class RegisterView(FormView):
    """ 用户注册View """
    form_class = RegisterForm
    template_name = 'user/registration_form.html'
    send_type = 'register'  # 邮件发送类型

    def form_valid(self, form):
        # 通过表单验证
        s = get_setting()  # 网站一些配置信息 blog.models.Setting
        user = form.save(commit=False)

        if s.user_verify_email:
            # 用户注册需要验证邮箱, 需要启动celery的消息队列
            code_str = self.generate_random_str()  # 验证码
            email = user.email  # 收件方
            task_obj = send_email_task.delay(email, code_str, self.send_type)  # celery异步任务对象

            # create里会进行save()
            EmailVerifyCode.objects.create(email=email, code=code_str, type=self.send_type, task_id=task_obj.task_id)

            user.is_active = False  # 未激活
            user.save()
            url = reverse('user:login')
            messages.success(self.request, '注册成功,前往邮箱激活')
        else:
            # 用户注册不需要验证邮箱
            user.save()
            login(self.request, user)  # 注册后的自动登录
            url = reverse('blog:index')
            messages.success(self.request, '注册成功, 欢迎加入本博客系统')

        if s.enable_multi_user:
            try:
                # 添加一个组
                res = Group.objects.get_or_create(name='register_user_group')
                register_user_group = res[0]

                # 添加一系列权限, 暂时就只给用户对自己文章的增删改查, view_model
                p1 = Permission.objects.get(codename='add_article')  # 增
                p2 = Permission.objects.get(codename='delete_article')  # 删
                p3 = Permission.objects.get(codename='change_article')  # 改
                p4 = Permission.objects.get(codename='view_article')  # 查
                register_user_group.permissions.add(p1, p2, p3, p4)

                # register_user_group.user_set.add(user)  # 两种方式都可以加入组
                user.groups.add(register_user_group)
                user.is_staff = True
                user.save()
            except Exception as e:
                logger.error(e)

        return HttpResponseRedirect(url)

    @staticmethod
    def generate_random_str(str_len=8):
        """ 生成长度为str_len的随机字符串 """
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        length = len(chars)
        random = Random()
        from functools import reduce

        _str = reduce(lambda x, y: x + y, [chars[random.randint(0, length - 1)] for _ in range(str_len)])
        return _str


class LoginView(FormView):
    """ 用户登陆View """
    form_class = LoginForm
    redirect_field_name = REDIRECT_FIELD_NAME  # 'next'
    template_name = 'user/login.html'
    redirect_authenticated_user = False  # 已登录用户访问login的url, 是否重定向
    success_url = '/'

    @method_decorator(sensitive_post_parameters())  # 保护post请求中的敏感数据, 错误信息会显示****
    @method_decorator(csrf_protect)  # 为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):  # 读一读django自带的LoginView dispatch源码
        # 已登陆用户重定向
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # 给上下问context增加变量
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to is None:
            redirect_to = self.success_url
        kwargs['redirect_to'] = redirect_to

        return super().get_context_data(**kwargs)  # 父类方法中会 Insert the form into the context dict

    def form_valid(self, form):  # TOREAD
        # 表单通过了验证
        login(self.request, form.get_user())
        # return super().form_valid(form)  # 这行父类就是调用了下行
        return HttpResponseRedirect(self.get_success_url())

    # def form_invalid(self, form):
    #     pass

    def get_success_url(self):
        url = self.get_redirect_url()
        return url

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        url_is_safe = is_safe_url(
            url=redirect_to,
            allowed_hosts=[self.request.get_host()],
            # require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else self.success_url


class LogoutView(RedirectView):
    """ 用户登出 """
    url = '/login/'  # 重定向后的url

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        logout(request)  # 登出
        return super().dispatch(request, *args, **kwargs)


class ActiveView(View):
    """ 用户激活邮箱 """

    def get(self, request, code):
        code_obj = EmailVerifyCode.objects.filter(code=code, type='register').last()  # last取默认排序后的最后一个
        # timestamp = (now() - code_obj.add_time).total_seconds()

        # 验证码过期以后再做吧, 不然又得要写多一个重发验证码
        if code_obj:  # and timestamp < 600:
            user = get_object_or_404(User, email=code_obj.email, is_active=False)
            user.is_active = True
            code_obj.is_used = True
            user.save()
            code_obj.save()

            login(request, user)
            messages.success(request, '激活成功, 欢迎加入本博客系统')
            return redirect(reverse('blog:index'))

        messages.success(request, '验证码有误')
        return redirect(reverse('user:login'))


@login_required
def refresh_cache(request):
    """ 清空缓存 """
    if request.user.is_superuser:
        from django.core.cache import cache
        if cache and cache is not None:
            cache.clear()

        messages.success(request, '缓存刷新成功')
        return redirect(reverse('blog:index'))
    else:
        return HttpResponseForbidden()  # 403封装的HttpResponse
