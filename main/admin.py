from django.contrib import admin

from goods.models import Categories, Products
# Register your models here.

# admin.site.register(Catigories)
# admin.site.register(Products)


@admin.register(Categories)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
