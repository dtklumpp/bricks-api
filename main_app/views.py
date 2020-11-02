from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project
from .models import Category

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return JsonResponse({"reply": "hiya"})
    # return HttpResponse('<h1>Hiya!</h1>')

@csrf_exempt
def homer(request):
    import json
    pull_var = json.loads(request.body).get("message")
    print("message: "+pull_var)
    return JsonResponse({"response": pull_var})
