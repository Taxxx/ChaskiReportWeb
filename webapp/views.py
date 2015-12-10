from django.shortcuts import render

# Create your views here.

#DJANGO REST FRAMEWORK
from rest_framework import viewsets
from webapp.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer