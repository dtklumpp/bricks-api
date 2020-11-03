from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=2500, null=True, blank=True)

    continent = models.CharField(max_length=50, default="North America")
    goal = models.IntegerField(default=100000)
    
    funding = models.IntegerField(default=0)
    pledges = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=250)

    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2500, null=True, blank=True)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

