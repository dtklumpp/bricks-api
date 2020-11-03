from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('homer/', views.homer, name='homer'),
    path('projects/', views.project_index, name='project_index'),
    path('projects/create', views.project_create, name='project_create'),
    path('projects/delete/<int:proj_id>', views.project_delete, name='project_delete'),
]
