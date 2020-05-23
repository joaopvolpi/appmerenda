from rest_framework import serializers
from .views import *
from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer
from djoser.conf import settings

#Overwrite do Djoser

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['email', 'first_name', 'last_name', 'tel', 'foto_rosto', 'foto_frente', 'foto_tras', 'quero_doar']




