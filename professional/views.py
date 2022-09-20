from django.shortcuts import render
from . models import Experience, Education, Skill
from intro.models import Personal
# Create your views here.

def professional(request):
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()

    data = {
        "experiences" : experiences,
        "educations" : educations,
        "skills" : skills,
        "details" : Personal.objects.get(id=1)
    }

    return render(request, "professional.html", data)
