from django.forms import ModelForm
from .models import Project
from .models import Comment


class Project_Form(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'image', 'description', 'continent', 'goal']

class Comment_Form(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'description']

class Pledge_Form(ModelForm):
    class Meta:
        model = Project
        fields = ['funding', 'pledges']
