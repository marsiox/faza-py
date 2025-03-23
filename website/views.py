from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

import requests

templates = {
    "home": "index.html",
    "o-nas": "o-nas.html",
    "kontakt": "kontakt.html",
    "usługi-elektryczne": "usługi-elektryczne.html",
    "pomiary-elektryczne": "pomiary-elektryczne.html",
    "pogotowie-elektryczne-trójmiasto": "pogotowie-elektryczne-trójmiasto.html",
    "instalacje-elektryczne": "instalacje-elektryczne.html",
  }

page_titles = {
  "home": "Faza-Ekspert • Elektryk Gdańsk, Gdynia, Sopot",
  "o-nas": "Info • Faza-Ekspert",
  "kontakt": "Kontakt • Faza-Ekspert",
  "usługi-elektryczne": "Usługi Elektryczne w Trójmieście • Faza-Ekspert",
  "pomiary-elektryczne": "Pomiary Elektryczne w Trójmieście",
  "pogotowie-elektryczne-trójmiasto": "Trójmiejskie Pogotowie Elektryczne",
  "instalacje-elektryczne": "Instalacje Elektryczne • Faza-Ekspert",
  "wycena": "Wyceń Instalację Elektryczną Online",
}

def dynamic(request, name):
  template_name = templates.get(name, "404.html")

  return render(request, "layout.html", {
    "content_template": template_name,
    "title": page_titles.get(name, "404"),
    "page_name": name
  })


def wycena(request):
  return render(request, "layout.html", {
    "content_template": "wycena.html",
    "title": page_titles.get("wycena", "404"),
    "page_name": "wycena",
  })