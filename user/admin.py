from django.contrib import admin


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'nickname', 'email')  # 列表显示的字段
    list_display_links = ('id', 'username', 'nickname', 'email')  # 列表页可以跳转到详情页的字段
