from django.contrib.auth.models import User, Group
from models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categoria
		fields = ('nombre',)

class ReportajeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Reportaje
		fields = ('titulo','lead','nota','tags','fecha','estado','reportero','categoria')

class ImagenSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Imagen
		fields = ('imagen','titulo','reportaje')

class AudioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Audio
		fields = ('audio','titulo','reportaje')

class VideoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Video
		fields = ('video','titulo','reportaje')