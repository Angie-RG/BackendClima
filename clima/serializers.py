from rest_framework import serializers
from . import models

class BusquedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Busqueda
        fields = '__all__'