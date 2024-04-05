from django.contrib import admin

from .models import Technology, Link, Project

# Register your models here.


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ["technologies"]
    inlines = [LinkInline]
