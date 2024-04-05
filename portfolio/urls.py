from django.urls import path

from portfolio import views

app_name = "portfolio"

urlpatterns = [
    # Portfolio
    path("", views.hello_world, name="hello_world"),
]
