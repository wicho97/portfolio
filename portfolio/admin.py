from django.contrib import admin

from .models import Technology, Project, Experience

# Register your models here.


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ["technologies"]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass
