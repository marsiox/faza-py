from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

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

def submit_email(request):
  if request.method == 'POST':
    email = request.POST.get('email')

    if email:
      try:
        send_mail(
          subject="Email ze strony Faza-Ekspert",
          message=email,
          from_email=settings.EMAIL_HOST_USER,
          recipient_list=[settings.EMAIL_TO],
          fail_silently=False,
        )
        return HttpResponse("Dziękujemy <a href='/'>wróć na stronę główną</a>")
      except Exception as e:
        return HttpResponse(f"Failed to send email: {str(e)}")
    else:
      return HttpResponse("Invalid email address!")
  return HttpResponse("Invalid request method.")
