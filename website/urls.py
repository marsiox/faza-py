from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap

app_name = "website"

sitemaps = {
  "static": StaticViewSitemap,
}

urlpatterns = [
  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
  path("", views.dynamic, {"name": "home"}, name="home"),
  path("<str:name>", views.dynamic, name="dynamic"),
  path('submit-email', views.submit_email, name='submit_email'),
]
