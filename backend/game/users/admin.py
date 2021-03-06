from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User, Profile

admin.site.register(Profile)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', )
        }),
    )
    limited_fieldsets = (
        (None, {
            'fields': ('username', )
        }),
        ('Personal info', {
            'fields': (
                'first_name',
                'last_name',
            )
        }),
        ('Important dates', {
            'fields': ('last_login', )
        }),
    )
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': ('username', 'password1', 'password2')
    }), )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = auth_admin.AdminPasswordChangeForm
    list_display = ('username', 'first_name', 'last_name', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('first_name', 'last_name', 'username')
    ordering = ('username', )
    readonly_fields = ('last_login', )
