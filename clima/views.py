from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import generics
from .models import Busqueda
from .serializers import BusquedaSerializer

# GET
class HistorialViewList(generics.ListAPIView):
    queryset = Busqueda.objects.all()
    serializer_class = BusquedaSerializer

# POST
@method_decorator(csrf_exempt, name='dispatch')
class HistorialCreateView(generics.CreateAPIView):
    queryset = Busqueda.objects.all()
    serializer_class = BusquedaSerializer
