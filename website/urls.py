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
  path("wycena", views.wycena, name="wycena"),
  path("", views.dynamic, {"name": "home"}, name="home"),
  path("<str:name>", views.dynamic, name="dynamic"),
]
