from rest_framework.permissions import IsAdminUser

from ..serializers import FullUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.response import Response
User = get_user_model()
from rest_framework.views import APIView

class UserList(generics.ListCreateAPIView):
    permission_classes=[IsAdminUser]
    serializer_class = FullUserSerializer


    def list(self, request):
        queryset = self.get_queryset()
        serializer = FullUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return User.objects.filter(validado=False, is_staff=False)

class UserDetail(generics.RetrieveUpdateAPIView):
    permission_classes=[IsAdminUser]
    queryset = User.objects.filter(validado=False, is_staff=False)
    serializer_class = FullUserSerializer

'''
mandar um patch request
{
	"validado": true
}
'''