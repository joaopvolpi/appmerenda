from rest_framework.permissions import IsAdminUser
from ..permissions import OwnerPraVer, AdminPodeTudoAutenticadoSoLe, QueroDoar
from ..serializers import MarmitaSerializer
from ..models import Marmita
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
User = get_user_model()
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
'''
class Solicitacao(APIView):
    def get(self, request, pk):
        marmita = Marmita.objects.get

'''