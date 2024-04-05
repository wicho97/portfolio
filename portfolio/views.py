from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


from .models import Project

# Create your views here.


def hello_world(request):
    projects = Project.objects.prefetch_related("links", "technologies")
    return render(
        request,
        "portfolio/home.html",
        {
            "projects": projects,
        },
    )
