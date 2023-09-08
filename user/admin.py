from django.contrib import admin

from user.models import UserCustom


@admin.register(UserCustom)
class UserCustomAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'avatar', 'role',
    )

