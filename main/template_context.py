from .models import Product, ProductAttribute


def get_filters(request):
    cats = Product.objects.distinct().values('category__title', 'category_id')
    brands = Product.objects.distinct().values('brand__title', 'brand_id')
    colors = ProductAttribute.objects.distinct().values('color__title', 'color_id', 'color__color_code')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size_id')
    date = {'cats': cats,
            'brands': brands,
            'colors': colors,
            'sizes': sizes}
    return date
