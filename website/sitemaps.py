from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "monthly"
    protocol = 'https'  # Force HTTPS protocol

    def items(self):
      return [
        "home",
        "o-nas",
        "kontakt",
        "usługi-elektryczne",
        "pomiary-elektryczne",
        "pogotowie-elektryczne-trójmiasto",
        "instalacje-elektryczne",
        "wycena",
      ]

    def location(self, item):
      if item == 'home':
        return reverse('website:home')
      return reverse('website:dynamic', kwargs={'name': item})
