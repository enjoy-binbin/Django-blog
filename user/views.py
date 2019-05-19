from django.views.generic import FormView, RedirectView
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url

from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth import logout, login
from django.contrib.auth.models import Group, Permission

from .forms import RegisterForm, LoginForm


# django有一个 path('', include('django.contrib.auth.urls')),
# 有专门用于 登陆登出的View, 只是没有模板, 读一读里面的源码实现
class RegisterView(FormView):
    """ 用户注册View """
    form_class = RegisterForm
    template_name = 'user/registration_form.html'

    def form_valid(self, form):
        # 通过表单验证, 保存用户跳转到登陆页
        user = form.save(commit=False)
        # user.is_active = False  # 未激活
        user.save()
        login(self.request, user)
        url = reverse('user:index')

        # TODO: 多用户博客系统的权限控制
        # 添加一个组
        # res = Group.objects.get_or_create(name='register_user_group')
        # register_user_group = res[0]
        #
        # try:
        #     p1 = Permission.objects.get(codename='view_category')
        #     p2 = Permission.objects.get(codename='change_category')
        #     p3 = Permission.objects.get(codename='add_category')
        #     p4 = Permission.objects.get(codename='delete_category')
        #     p5 = Permission.objects.get(codename='view_article')
        #     p6 = Permission.objects.get(codename='change_article')
        #     p7 = Permission.objects.get(codename='add_article')
        #     p8 = Permission.objects.get(codename='delete_article')
        #     register_user_group.permissions.add(p1, p2, p3, p4, p5, p6, p7, p8)
        #     # register_user_group.user_set.add(user)
        #     user.groups.add(register_user_group)
        # except:
        #     pass

        return HttpResponseRedirect(url)


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
        auth.login(self.request, form.get_user())
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


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden


@login_required
def refresh_cache(request):
    try:
        if request.user.is_superuser:
            from django.core.cache import cache
            if cache and cache is not None:
                cache.clear()
            return HttpResponse('ok')
        else:
            return HttpResponseForbidden()  # 403封装的HttpResponse
    except Exception as e:
        return HttpResponse(e)
