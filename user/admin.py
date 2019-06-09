from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.admin.models import LogEntry, DELETION
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.html import format_html

User = get_user_model()


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'nickname', 'email', 'user_level')  # 列表显示的字段
    list_display_links = ('id', 'username', 'nickname', 'email', 'user_level')  # 列表页可以跳转到详情页的字段
    ordering = ('-is_superuser', '-is_staff', '-is_active')  # 默认排序
    list_filter = ('is_superuser', 'is_active')  # 过滤器
    date_hierarchy = 'add_time'  # 添加时间筛选
    search_fields = ('username', 'email', 'nickname')  # 可搜索的字段
    filter_horizontal = ('groups', 'user_permissions')  # 打横显示
    fieldsets = (  # 分块显示
        (None, {'fields': ('username', 'password')}),
        ('用户信息', {'fields': ('first_name', 'last_name', 'email')}),
        ('用户权限', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('日期相关', {'fields': ('last_login', 'date_joined')}),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        """ 获取页面表单 """
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields['password'].help_text = '管理员可以直接修密码，会自动进行加密操作'
        return form

    def save_model(self, request, obj, form, change):
        """ 保存model之前添加自己的逻辑 """
        if change:
            # obj是当前操作的对象, user对象是从数据库里查找出来的对象
            user = User.objects.get(id=obj.id)
            if obj.password != user.password:
                obj.set_password(obj.password)
                # obj.save()  # 在后面里有save
        else:
            # 增加用户, 就直接设置密码
            obj.set_password(obj.password)
        return super().save_model(request, obj, form, change)


class EmailVerifyCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'code', 'type', 'is_used', 'expired')
    list_display_links = ('id', 'email', 'code')


class LogEntryAdmin(admin.ModelAdmin):
    """ 日志管理 """
    date_hierarchy = 'action_time'  # 根据时间筛选
    list_display = ('action_time', 'user_link', 'content_type', 'get_the_object', 'get_change_message', 'action_flag')
    list_display_links = ('action_time', 'get_change_message')
    readonly_fields = [f.name for f in LogEntry._meta.fields] + \
                      ['get_the_object', 'content_type', 'user_link', 'get_change_message']
    fieldsets = (
        ('元信息', {'fields': ('action_time', 'user_link', 'action_flag', 'get_the_object',)}),
        ('其他信息', {'fields': ('object_id', 'object_repr', 'get_change_message', 'content_type',)}),
    )
    list_per_page = 15

    def has_add_permission(self, request):
        """ 不允许添加 """
        return False

    def user_link(self, obj):
        """ 链接到用户页面, obj是一个当前对象 """
        content_type = ContentType.objects.get_for_model(obj.user)
        app_label = content_type.app_label  # obj.user._meta.app_laebl
        model_name = content_type.model  # obj.user._meta.model_name
        link = reverse('admin:%s_%s_change' % (app_label, model_name), kwargs={'object_id': obj.user_id})
        return format_html('<a href="%s">%s</a>' % (link, obj.user))

    user_link.short_description = '操作用户'
    user_link.admin_order_field = 'user'  # 根据哪个字段排序

    def get_change_message(self, obj):
        """
        会将json格式的消息翻译成字符串
        [{"changed": {"fields": ["password", "last_login"]}}] --> 已修改password 和 last_login。
        """
        return obj.get_change_message()

    get_change_message.short_description = '修改消息'

    def get_the_object(self, obj):
        if obj.action_flag == DELETION:  # 添加是1, 修改是2, 删除是3
            link = obj.object_repr  # 操作对象的呈现, 其实应该就是str(obj)
        else:
            link = obj.get_admin_url()  # 会获取到当时操作对象的链接地址
            link = format_html('<a href="%s">%s</a>' % (link, obj.object_repr))
        return link

    get_the_object.short_description = '操作对象'
