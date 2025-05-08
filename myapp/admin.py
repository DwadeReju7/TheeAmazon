from django.contrib import admin
from .models import Customer, Categories, Products, Order, Order_Items

admin.site.register(Customer)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Order_Items)
# Register your models here.
