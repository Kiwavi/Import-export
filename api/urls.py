from django.urls import path
from .views import ForexAPIView


urlpatterns = [
    path('', ForexAPIView.as_view()),
]
