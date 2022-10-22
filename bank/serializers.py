from rest_framework import serializers
from .models import Comptesespece, Imputationsespeces


class ComptesespeceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comptesespece
        fields = '__all__'

class ImputationsespecesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imputationsespeces
        fields = '__all__'
