from django.urls import path, include
from .views import *
from api import views

urlpatterns = [
    path('naovalidados/', UserList.as_view()),              #RETORNA A LISTA DE USERS AINDA NAO VALIDADOS PELO ADMIN
    path('naovalidados/<int:pk>/', UserDetail.as_view()),   #UM PATCH AQUI PRA EDITAR O USER E VALIDA-LO PELO ADMIN
    path('marmitas/', MarmitaList.as_view()),               #LISTA DE MARMITAS DISPONIVEIS
    path('marmitas/<int:pk>/', MarmitaDetail.as_view()),    #DETALHE DA MARMITA
    path('marmitas/<int:pk>/solicitar/', SolicitacaoView.as_view()),   #POST PRA SOLICITAR
    path('minhas_solicitacoes/', ListaSolicitacaoView.as_view()),      #VER MARMITA SOLICITADA
    path('solicitaram_minha_marmita/', PessoasQueSolicitaramMinhaMarmitaView.as_view()),     #O DOADOR VÊ QUEM PEDIU
]