from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'email',
        'role',
    )
    search_fields = (
        'username',
        'email',
    )
    list_filter = ('role',)
    list_editable = ('role',)
    empty_value_display = '--empty--'


admin.site.register(User, UserAdmin)
