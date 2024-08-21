
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('related', views.related, name='related'),
]

   









   