from django.contrib import admin


def enable_or_disable_config(modeladmin, request, queryset):
    """ 启用或禁用对应的设置项 """
    for config in queryset:
        config.is_enable = False if config.is_enable else True
        config.save()


enable_or_disable_config.short_description = '启用或禁用对应的设置项'


class OAuthConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'is_enable', 'add_time', 'modify_time')
    list_display_links = ('id', 'type')
    actions = (enable_or_disable_config,)


class OAuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'nickname', 'email')
    list_display_links = ('id', 'type', 'nickname', 'email')
    search_fields = ('nickname', 'email', 'type')
    list_filter = ('type',)
    list_per_page = 20

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in obj._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return True
