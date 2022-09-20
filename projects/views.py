from django.shortcuts import render

from . models import Project, Certificate, Achievement

# Create your views here.
def projects(request):

    data = {
        "projects" : Project.objects.all(),
        "certificates" : Certificate.objects.all(),
        "achievements": Achievement.objects.all()
    }

    return render(request, "projects.html",data)
