from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'color', 'size', 'price', 'status')
    list_editable = ('status',)


admin.site.register(Product,ProductAdmin)
