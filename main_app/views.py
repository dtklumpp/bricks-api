from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project
from .models import Category
from .models import Comment

from .forms import Project_Form
from .forms import Comment_Form
from .forms import Pledge_Form


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

# category index

def category_index(request):
    categories = list(Category.objects.values().all())
    return JsonResponse({'data': categories})



# projects CRUD

def project_index(request):
    projects = list(Project.objects.values().all())
    return JsonResponse({'data': projects})

def project_view(request, proj_id):
    project = Project.objects.values().get(id=proj_id)
    return JsonResponse({'data': project})

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


@csrf_exempt
def project_pledge(request, proj_id):
    project = Project.objects.get(id=proj_id)
    import json
    pull_var = json.loads(request.body)
    update = pull_var
    print("pullvar:")
    print(pull_var)
    print("update:")
    print(update)
    update['funding'] = project.funding + int(pull_var['pledge'])
    update['pledges'] = project.pledges + 1

    pledge_form = Pledge_Form(update, instance=project)
    if pledge_form.is_valid():
        old_project = pledge_form.save(commit=False)
        old_project.save()
    return JsonResponse({"new amount": old_project.funding, "new pledges": old_project.pledges})

def project_filter(request, cat_id):
    category = Category.objects.get(id=cat_id)
    projects = list(category.projects.values())
    return JsonResponse({'data': projects})

def project_truncate(request, cutoff):
    projects = list(Project.objects.values().all())
    projectsBrief = projects[:cutoff]
    return JsonResponse({'data': projectsBrief})


def project_location(request, country):

    nam_cont = ["USA", "MEX", "CAN", "CUB", "GTM", "HND", "NIC", "CRI", "PAN", "HTI", "DOM"]
    sam_cont = ["BRA", "FRA", "SUR", "GUY", "VEN", "COL", "ECU", "PER", "BOL", "PRY", "ARG", "URY", "CHL"]
    eur_cont = ["GRC", "ALB", "MKD", "BGR", "XKX", "MNE", "BIH", "SRB", "ROU", "HRV", "HUN", "SVN", "AUT", "CZE", "SVK", "UKR", "MDA", "TUR", "BLR", "POL", "EST", "LVA", "LTU", "CZE", "CHE", "ITA", "PRT", "ESP", "FRA", "BEL", "NLD", "LUX", "DEU", "DNK", "IRL", "GBR", "NOR", "SWE", "FIN"]
    aus_cont = ["AUS"]
    azn_cont = ["USA", "RUS", "CHN", "AUS", "NZL", "AUS", "PNG", "IDN", "IDN", "IDN", "IDN", "PHL", "MYS", "MYS", "JPN", "KOR", "PRK", "TWN", "CHN", "VNM", "KHM", "MYS", "THA", "THA", "LAO", "MMR", "IND", "CHN", "MNG", "RUS", "BTN", "BGD", "NPL", "IND", "IND", "PAK", "AFG", "TJK", "KGZ", "UZB", "TKM", "KAZ", "IRN", "AZE", "GEO", "ARM", "RUS", "SYR", "IRQ", "JOR", "SAU", "OMN", "YEM", "ARE", "ISR"]
    afr_cont = ["COD", "GAB", "COG", "GNQ", "CMR", "CAF", "TCD", "NER", "NGA", "BEN", "BFA", "TGO", "GHA", "CIV", "LBR", "SLE", "GIN", "MLI", "GNB", "SEN", "SEN", "MRT", "ESH", "MAR", "ESH", "DZA", "TUN", "LBY", "EGY", "SDN", "SSD", "ETH", "ERI", "SOL", "SOM", "KEN", "UGA", "TZA", "BDI", "RWA", "MDG", "MOZ", "MWI", "MWI", "MWI", "ZMB", "MOZ", "ZWE", "ZAF", "SWZ", "LSO", "BWA", "NAM", "AGO", "AGO", "ZMB"]

    if country in nam_cont:
        location = "North America"
    elif country in sam_cont:
        location = "South America"
    elif country in eur_cont:
        location = "Europe"
    elif country in aus_cont:
        location = "Australia"
    elif country in azn_cont:
        location = "Asia"
    elif country in afr_cont:
        location = "Africa"
    else:
        location = "North America"

    projects = list(Project.objects.values().filter(continent=location))
    return JsonResponse({'data': projects})









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
