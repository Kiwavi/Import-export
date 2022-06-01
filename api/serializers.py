from rest_framework import serializers
from appimports.models import Currency


class ForexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('Date', 'Dollar', 'Pound', 'Euro')
