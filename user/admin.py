from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'nickname', 'email', 'user_level')  # 列表显示的字段
    list_display_links = ('id', 'username', 'nickname', 'email', 'user_level')  # 列表页可以跳转到详情页的字段
    ordering = ('-is_superuser', '-is_staff', '-is_active')  # 默认排序
    list_filter = ('is_superuser', 'is_active')  # 过滤器
    date_hierarchy = 'add_time'  # 添加时间筛选
    # fieldsets = (('用户信息', {'fields': ('username', 'email', 'password')}),)  # 分块显示
    search_fields = ('username', 'email', 'nickname')  # 可搜索的字段

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
        return super().save_model(request, obj, form, change)


class EmailVerifyCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'code', 'type', 'is_used', 'expired')
    list_display_links = ('id', 'email', 'code')
