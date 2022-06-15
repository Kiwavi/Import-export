from django.shortcuts import render
from rest_framework import generics
from appimports.models import Currency
from .serializers import ForexSerializer

# Create your views here.


class ForexAPIView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = ForexSerializer


class ForexTwoAPIView(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = ForexSerializer
    
