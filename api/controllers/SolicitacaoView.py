from rest_framework.permissions import IsAdminUser
from ..permissions import OwnerPraVer, AdminPodeTudoAutenticadoSoLe, QueroDoar
from ..serializers import MarmitaSerializer, FullUserSerializer, MarmitaProntaSerializer
from ..models import Marmita
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
User = get_user_model()
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status

class SolicitacaoView(APIView):

    def post(self, request, pk):
        marmita = get_object_or_404(Marmita, pk=pk)
        '''
        if marmita.solicitacao.filter(id=request.user.id).exists():
            return Response(data={ "message": "Solicitação já  foi enviada!" }, status=status.HTTP_200_OK)
        else:
            marmita.solicitacao.add(request.user)
            marmita.update(solicitada=True)
            return Response(data={ "message": "Marmita solicitada!" }, status=status.HTTP_200_OK)

        '''
        if marmita.solicitacao==request.user:
            return Response(data={ "message": "Solicitação já  foi enviada!" }, status=status.HTTP_200_OK)
        else:
            Marmita.objects.filter(pk=pk).update(solicitacao=request.user, solicitada=True)
            return Response(data={ "message": "Marmita solicitada!" }, status=status.HTTP_200_OK)

class ListaSolicitacaoView(APIView):
    def get(self, request):
        user = request.user
        lista_sols = user.solicitacao.all()            
        data = MarmitaSerializer(lista_sols, many=True).data

        return Response(data)


class PessoasQueSolicitaramMinhaMarmitaView(APIView):
    def get(self, request):
        user = request.user
        lista_marmitas = Marmita.objects.filter(usuario=request.user, solicitada=True)          
        #lista_users = User.objects.filter(solicitacao=request.user)          
        data = MarmitaProntaSerializer(lista_marmitas, many=True).data

        return Response(data)