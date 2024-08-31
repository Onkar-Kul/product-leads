from django.db import models

from products.models import Product


# Create your models here.


class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    interested_products = models.ManyToManyField(Product, related_name='lead_interested_products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
