from django.contrib import admin

from .models import UserProfile
from binblog.admin import admin_site


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin_site.register(UserProfile, UserProfileAdmin)
