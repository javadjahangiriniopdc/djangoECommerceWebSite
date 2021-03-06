from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Brand)

admin.site.register(Size)


class BannerAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'image_tag')


admin.site.register(Banner, BannerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')


admin.site.register(Category, CategoryAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_bg')


admin.site.register(Color, ColorAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'brand', 'status', 'is_featured')
    list_editable = ('status', 'is_featured')


admin.site.register(Product, ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'product', 'color', 'size', 'price')


admin.site.register(ProductAttribute, ProductAttributeAdmin)


# order
class CartOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amt', 'paid_status', 'order_dt')


admin.site.register(CartOrder, CartOrderAdmin)


# order
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ('order', 'invoice_no', 'item', 'image_tag', 'qty', 'price', 'total')


admin.site.register(CartOrderItem, CartOrderItemsAdmin)
