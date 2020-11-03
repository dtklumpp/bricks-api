from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project
from .models import Category
from .models import Comment

from .forms import Project_Form
from .forms import Comment_Form


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



# projects CRUD

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
        new_project.save()
        # here is where would attach to other models and stuff
        cat1 = Category.objects.get(id=1)
        cat1.projects.add(new_project.id)
        cat1.save()
        
        print(new_project.id)
        print(new_project)
        made_project = Project.objects.values().get(id=new_project.id)
        # new_reply = new_project.values()
        return JsonResponse({"return:": made_project})
    else:
        return JsonResponse({"return:": "bad_input"})

@csrf_exempt
def project_delete(request, proj_id):
    doomed_project = Project.objects.get(id=proj_id)
    doomed_project.delete()
    return JsonResponse({"deleted project": proj_id})

@csrf_exempt
def project_edit(request, proj_id):
    project = Project.objects.get(id=proj_id)
    import json
    pull_var = json.loads(request.body)

    project_form = Project_Form(pull_var, instance=project)
    if project_form.is_valid():
        old_project = project_form.save(commit=False)
        old_project.save()
    return JsonResponse({"edited project": proj_id})

# comments CRD

@csrf_exempt
def comment_create(request, proj_id):
    import json
    pull_var = json.loads(request.body)

    comment_form = Comment_Form(pull_var)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.project_id = proj_id
        new_comment.save()
        
        made_comment = Comment.objects.values().get(id=new_comment.id)
        # new_reply = new_comment.values()
        return JsonResponse({"return:": made_comment})
    else:
        return JsonResponse({"return:": "bad_input"})

@csrf_exempt
def comment_delete(request, comm_id):
    doomed_comment = Comment.objects.get(id=comm_id)
    doomed_comment.delete()
    return JsonResponse({"deleted comment": comm_id})

def comment_index(request, proj_id):
    # comments = list(Comment.objects.values().all())
    comments = list(Comment.objects.values().filter(project_id=proj_id))
    return JsonResponse({'data': comments})
