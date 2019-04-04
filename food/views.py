from django.shortcuts import render
from rest_framework import viewsets
from .models import listing
from .serializers import LagSer

class FoodView(viewsets.ModelViewSet):
    queryset = listing.objects.all()
    serializer_class = LagSer
