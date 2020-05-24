from rest_framework.permissions import IsAdminUser
from ..permissions import QueroDoar
from ..serializers import MarmitaSerializer, FullUserSerializer, MarmitaProntaSerializer
from ..models import Marmita
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.response import Response
User = get_user_model()
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status
#from datetime import date

class SolicitacaoView(APIView):

    def post(self, request, pk):
        '''
        marmitas_ja_solicitadas = Marmita.objects.filter(solicitacao=request.user)
        for marmitex in marmitas_ja_solicitadas:
            if marmitex.hora_solicitacao==date.today():
                return Response(data={ "message": "Você já solicitou uma marmita hoje!" }, status=status.HTTP_200_OK)
        '''
        marmita = get_object_or_404(Marmita, pk=pk)

        if marmita.solicitacao==request.user:
            return Response(data={ "message": "Solicitação já  foi enviada!" }, status=status.HTTP_200_OK)
        else:
            Marmita.objects.filter(pk=pk).update(solicitacao=request.user, solicitada=True)  #, hora_solicitacao=date.today()
            return Response(data={ "message": "Marmita solicitada!" }, status=status.HTTP_200_OK)

class ListaSolicitacaoView(APIView):
    def get(self, request):
        user = request.user
        lista_sols = user.solicitacao.all()            
        data = MarmitaSerializer(lista_sols, many=True).data

        return Response(data)


class PessoasQueSolicitaramMinhaMarmitaView(APIView):
    permission_classes=[QueroDoar]
    def get(self, request):
        user = request.user
        lista_marmitas = Marmita.objects.filter(usuario=request.user, solicitada=True)         
        data = MarmitaProntaSerializer(lista_marmitas, many=True).data

        return Response(data)