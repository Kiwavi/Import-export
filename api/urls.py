from django.urls import path
from .views import ForexAPIView, ForexTwoAPIView


urlpatterns = [
    path('forex', ForexAPIView.as_view()),
    path('forextwo', ForexTwoAPIView.as_view()),
]
