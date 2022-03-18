from django.shortcuts import render
from .models import Category


# Create your views here.
def home(request):
    return render(request, 'index.html')


# category
def category_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'category_list.html', {'data': data})
