from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
  path("", views.dynamic, {"name": "home"}, name="home"),
  path("<str:name>.html", views.dynamic, name="dynamic"),
]
