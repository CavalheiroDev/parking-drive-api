from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'cpf')
    list_filter = ('email', 'first_name')
    search_fields = ('email',)
    ordering = ('first_name', 'last_name', 'email',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
    )

admin.site.register(User, CustomUserAdmin)
