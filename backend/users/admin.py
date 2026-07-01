from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'name', 'role', 'verification_status', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {
            'fields': (
                'role',
                'name',
                'phone',
                'specialty',
                'license_number',
                'license_document_url',
                'verification_status'
            )
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
