from django.contrib import admin
from .models import Category, Color, Size, Brand, Product, Banner, ProductAttribute

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "brand",
        "color",
        "size",
        "status",
    ]
    list_editable = ("status",)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product",
        "price",
        "color",
        "size",
    ]


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(Color)
admin.site.register(Size)
