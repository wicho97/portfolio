from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


from .models import Project, Technology, Experience, Information, Social

# Create your views here.


def home(request):
    projects = Project.objects.prefetch_related("technologies")
    technologies = Technology.objects.all()
    experiences = Experience.objects.all().order_by("-id")
    information = Information.objects.all().first()
    socials = Social.objects.all().first()

    return render(
        request,
        "portfolio/home.html",
        {
            "projects": projects,
            "technologies": technologies,
            "experiences": experiences,
            "information": information,
            "socials": socials,
        },
    )
