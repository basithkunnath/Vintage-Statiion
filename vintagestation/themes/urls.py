from django.urls import path
from . import views
urlpatterns = [
    path('theme', views.Theme, name='theme'),
]
