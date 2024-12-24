from django.shortcuts import render

def dynamic(request, name):
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
    "pomiary-elektryczne": "Pomiary Elektryczne w Trójmieście • Faza-Ekspert",
    "pogotowie-elektryczne-trójmiasto": "Trójmiejskie Pogotowie Elektryczne • Faza-Ekspert",
    "instalacje-elektryczne": "Instalacje Elektryczne • Faza-Ekspert",
  }

  template_name = templates.get(name, "404.html")

  return render(request, "layout.html", {
    "content_template": template_name,
    "title": page_titles.get(name, "404")
  })