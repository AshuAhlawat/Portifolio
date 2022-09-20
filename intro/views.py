from django.shortcuts import render
from .models import Personal



def intro(request):
    details = Personal.objects.get(id=1)

    data = {
        "details":details
    }
    
    return render(request, "intro.html", data)
