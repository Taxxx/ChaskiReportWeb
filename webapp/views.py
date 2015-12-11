from django.shortcuts import render
from webapp.models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#DJANGO REST FRAMEWORK
from rest_framework import viewsets
from webapp.serializers import *

@csrf_exempt
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@csrf_exempt
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@csrf_exempt
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

@csrf_exempt
class ReportajeViewSet(viewsets.ModelViewSet):
    queryset = Reportaje.objects.all()
    serializer_class = ReportajeSerializer

@csrf_exempt
class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer

@csrf_exempt
class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

@csrf_exempt
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer