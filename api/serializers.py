from rest_framework import serializers
from .views import *
from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer
from djoser.conf import settings

#Overwrite do Djoser

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['email', 'first_name', 'last_name', 'tel', 'foto_rosto', 'foto_frente', 'foto_tras', 'quero_doar', 'endereco']

class FullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions']

class MiniUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'tel', 'endereco']

class MiniUserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'tel', 'foto_rosto']


class MarmitaSerializer(serializers.ModelSerializer):
    usuario = MiniUserSerializer(read_only=True)
    class Meta:
        model = Marmita
        exclude = ['solicitacao', 'solicitada', 'hora_solicitacao']

class MarmitaProntaSerializer(serializers.ModelSerializer):
    solicitacao = MiniUserSerializer2(read_only=True)
    
    class Meta:
        model = Marmita
        exclude = ['usuario', 'solicitada']