from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('homer/', views.homer, name='homer'),
]
