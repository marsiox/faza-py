from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

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
  if request.method == "POST":
    costs = calculate_quotation(request)

    return render(request, "layout.html", {
      "content_template": "wycena-wynik.html",
      "title": page_titles.get("wycena", "404"),
      "page_name": "wycena",
      **costs
    })

  return render(request, "layout.html", {
    "content_template": "wycena.html",
    "title": page_titles.get("wycena", "404"),
    "page_name": "wycena",
  })


def calculate_quotation(request):
  rooms_str = request.POST.get("rooms")
  sockets_str = request.POST.get("sockets")
  lights_str = request.POST.get("lights")
  phases_str = request.POST.get("phases")

  # Parse input
  rooms = int(rooms_str) if rooms_str else 0
  sockets = int(sockets_str) if sockets_str else 0
  lights = int(lights_str) if lights_str else 0
  phases = int(phases_str) if phases_str else 0

  has_washing_machine = request.POST.get("washing-machine") == "on"
  has_induction = request.POST.get("induction") == "on"
  has_fridge = request.POST.get("fridge") == "on"
  has_dryer = request.POST.get("dryer") == "on"

  # Validate input
  if rooms < 1:
    print("Invalid input")
    return {
      "hardware_cost": 0,
      "extra_circuits_cost": 0,
      "measurement_cost": 0,
      "distribution_board_cost": 0,
      "labour_cost": 0,
      "total_cost": 0,
    }

  # Define costs
  MEASUREMENT_COST = 300
  CIRCUIT_BREAKER_COST = 18
  AVG_CABLE_COST = 5
  LABOUR_PER_POINT_COST = 145

  # Calculate cable length

  total_cable_length = rooms * 25
  cables_cost = total_cable_length * AVG_CABLE_COST
  hardware_cost = cables_cost + ((sockets + lights) * 22)

  # Calculate costs

  extra_circuits = 0
  if has_washing_machine:
    extra_circuits += 1
  if has_induction:
    extra_circuits += 1
  if has_fridge:
    extra_circuits += 1
  if has_dryer:
    extra_circuits += 1

  extra_circuits_cost = extra_circuits * 200

  # Calculate circuits
  circuits = rooms * 2 + extra_circuits

  circuit_breakers_cost = circuits * CIRCUIT_BREAKER_COST
  rcds_cost = (200 * phases) + 300
  labour_cost = (sockets + lights) * LABOUR_PER_POINT_COST

  distribution_board_cost = circuit_breakers_cost + rcds_cost + 600

  total_cost = (
    extra_circuits_cost +
    MEASUREMENT_COST +
    distribution_board_cost +
    hardware_cost +
    labour_cost
)

  # Create a dictionary to pass context to the template
  return {
    "hardware_cost": hardware_cost,
    "extra_circuits_cost": extra_circuits_cost,
    "measurement_cost": MEASUREMENT_COST,
    "distribution_board_cost": distribution_board_cost,
    "labour_cost": labour_cost,
    "total_cost":  "{:,.2f}".format(total_cost),
  }

# def submit_email(request):
#   if request.method == "POST":
#     email = request.POST.get("email")

#     if email:
#       try:
#         send_mail(
#           subject="Email ze strony Faza-Ekspert",
#           message=email,
#           from_email=settings.EMAIL_HOST_USER,
#           recipient_list=[settings.EMAIL_TO],
#           fail_silently=False,
#         )
#         return HttpResponse("Dziękujemy <a href="/">wróć na stronę główną</a>")
#       except Exception as e:
#         return HttpResponse(f"Failed to send email: {str(e)}")
#     else:
#       return HttpResponse("Invalid email address!")
#   return HttpResponse("Invalid request method.")
