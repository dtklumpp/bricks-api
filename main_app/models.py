from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=2500, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=250)

    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name

