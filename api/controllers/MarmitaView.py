from rest_framework.permissions import IsAdminUser
from ..permissions import QueroDoar, Validado
from ..serializers import MarmitaSerializer
from ..models import Marmita
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
User = get_user_model()
from rest_framework.views import APIView

class MarmitaList(generics.ListCreateAPIView):
    permission_classes = [QueroDoar, Validado]
    serializer_class = MarmitaSerializer
    queryset = Marmita.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = MarmitaSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return Marmita.objects.filter(solicitada=False)


class MarmitaDetail(generics.RetrieveDestroyAPIView):
    permission_classes=[Validado]
    queryset = Marmita.objects.all()
    serializer_class = MarmitaSerializer
