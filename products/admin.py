from django.contrib import admin

from products.models import Product


# Register your models here.

@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product_name', 'description', 'price', 'created_at', 'updated_at'
    )
    search_fields = ('product_name', 'price')
