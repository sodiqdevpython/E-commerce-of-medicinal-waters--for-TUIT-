from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)

@admin.register(Customer)
class AdminViewCustomer(admin.ModelAdmin):
    search_fields = ['first_name','last_name','phone']
    list_display = ['first_name','last_name','phone','email']
    
@admin.register(Order)
class AdminViewOrder(admin.ModelAdmin):
    search_fields = ['address','phone','customer']
    list_display = ['customer','product','quantity','price','date','status']

    # ,'product','phone','email','quantity','price','phone','date'