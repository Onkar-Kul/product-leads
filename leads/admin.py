from django.contrib import admin

from leads.models import Lead


# Register your models here.


@admin.register(Lead)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'email', 'phone_number', 'created_at'
    )
    search_fields = ('name', 'email')
