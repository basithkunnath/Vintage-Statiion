from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import remove_from_cart

urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_success/', views.checkout_success, name='checkout_success'),
    path('remove/<int:item_id>/',remove_from_cart, name='remove_from_cart'),

    # Add other URL patterns here
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

