from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    # Blog
    path("", views.hello_world, name="hello_world"),
]