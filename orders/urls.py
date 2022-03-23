from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pro_id>', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart/<int:pro_id>', views.update_cart, name='update_cart'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]