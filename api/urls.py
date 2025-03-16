from django.urls import path
from .views import QuotationAPIView

urlpatterns = [
    path('get-a-quote/', QuotationAPIView.as_view(), name='calculate_price'),
]
