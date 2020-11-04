from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('homer/', views.homer, name='homer'),
    path('projects/', views.project_index, name='project_index'),
    path('projects/create', views.project_create, name='project_create'),
    path('projects/delete/<int:proj_id>', views.project_delete, name='project_delete'),
    path('projects/edit/<int:proj_id>', views.project_edit, name='project_edit'),
    path('projects/view/<int:proj_id>', views.project_view, name='project_view'),
    path('projects/pledge/<int:proj_id>', views.project_pledge, name='project_pledge'),
    path('projects/filter/<int:cat_id>', views.project_filter, name='project_filter'),


    # categories
    path('categories/', views.category_index, name='category_index'),



    # comments time
    path('comments/<int:proj_id>', views.comment_index, name='comment_index'),
    path('comments/create/<int:proj_id>', views.comment_create, name='comment_create'),
    path('comments/delete/<int:comm_id>', views.comment_delete, name='comment_delete'),

]
