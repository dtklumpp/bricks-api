from django.contrib import admin
from .models import Project
from .models import Category
from .models import Comment

# Register your models here.

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comment)
