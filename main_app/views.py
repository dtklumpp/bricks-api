from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project
from .models import Category

# Create your views here.

def home(request):
    return JsonResponse({"reply": "hiya"})
    # return HttpResponse('<h1>Hiya!</h1>')
