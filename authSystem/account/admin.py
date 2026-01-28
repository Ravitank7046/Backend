from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserModelAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_superuser','is_active',)
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    fieldsets = [
        ("User Credentials", {'fields': ['email', 'password']}),
        ('Personal Info', {'fields': ['name', 'city']}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login',)}),
    ]
    ordering = ["email",'id']
    filter_horizontal = []
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
admin.site.register(User,UserModelAdmin)