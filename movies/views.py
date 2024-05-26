from django.shortcuts import render
from rest_framework import viewsets
from .serializer import MovieSerializer
from .models import Moviedata

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class = MovieSerializer