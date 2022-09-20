from django.contrib import admin
from django.urls import path, include

from django.shortcuts import redirect

from django.conf.urls.static import static
from django.conf import settings


def to_home(request):
    return redirect("/intro")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("intro", include("intro.urls")),
    path("professional", include("professional.urls")),
    path("projects", include("projects.urls")),
    path("", to_home)
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
