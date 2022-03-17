from django.db import models


# Category
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cat_imgs/")

    def __str__(self):
        return self.title


# Brand
class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="brand_imgs/")

    def __str__(self):
        return self.title


# Color
class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# Size
class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# product Model
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product_imgs/")
    slug = models.CharField(max_length=400)
    detail = models.TextField()
    specs = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
