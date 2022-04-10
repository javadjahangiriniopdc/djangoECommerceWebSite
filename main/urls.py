from django.contrib import admin
from django.urls import path, include

from main import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('category-list', views.category_list, name='category-list'),
    path('brand-list', views.brand_list, name='brand-list'),
    path('product-list', views.product_list, name='product-list'),
    path('category-product-list/<int:cat_id>', views.category_product_list, name='category-product-list'),
    path('brand-product-list/<int:brand_id>', views.brand_product_list, name='brand-product-list'),
    path('product/<str:slug>/<int:id>', views.product_detail, name='product_detail'),
    path('filter-data', views.filter_data, name='filter_data'),
    path('load-more-data', views.load_more_data, name='load_more_data'),
    path('add-to-cart', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart_list, name='cart'),
    path('delete-from-cart', views.delete_from_cart, name='delete_from_cart'),
    path('update-cart', views.update_from_cart, name='update-cart'),
    path('accounts/singnup', views.signup, name='signup'),
    path('checkout', views.checkout, name='checkout'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
