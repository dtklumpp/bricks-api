from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project
from .models import Category

from .forms import Project_Form

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

def project_index(request):
    projects = list(Project.objects.values().all())
    return JsonResponse({'data': projects})

@csrf_exempt
def project_create(request):
    import json
    pull_var = json.loads(request.body)
    print("incoming: "+str(pull_var))

    project_form = Project_Form(pull_var)
    if project_form.is_valid():
        new_project = project_form.save(commit=False)
        # here is where would attach to other models and stuff
        new_project.save()
        print(new_project.id)
        print(new_project)
        made_project = Project.objects.values().get(id=new_project.id)
        # new_reply = new_project.values()
        return JsonResponse({"return:": made_project})
    else:
        return JsonResponse({"return:": "bad_input"})
