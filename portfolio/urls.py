from django.urls import path

from blog import views

app_name = "portfolio"

urlpatterns = [
    # Portfolio
    path("", views.hello_world, name="hello_world"),
]