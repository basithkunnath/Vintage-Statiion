from django.urls import path
from . import views
urlpatterns = [
    path('order', views.Order, name='cart'),
]
