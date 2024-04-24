from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


from .models import Project, Technology

# Create your views here.


def home(request):
    projects = Project.objects.prefetch_related("links", "technologies")
    technologies = Technology.objects.all()

    return render(
        request,
        "portfolio/home.html",
        {
            "projects": projects,
            "technologies": technologies
        },
    )
