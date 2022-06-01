from django.urls import path
from .views import ForexAPIView


urlpatterns = [
    path('forex', ForexAPIView.as_view()),
]
