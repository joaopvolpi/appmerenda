from django.urls import path, include
from .views import *
from api import views
from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register('', View)


urlpatterns = [
    #path('', include(router.urls))
    path('naovalidados/', UserList.as_view()),
    path('naovalidados/<int:pk>/', UserDetail.as_view()),
    path('marmitas/', MarmitaList.as_view()),
    path('marmitas/<int:pk>/', MarmitaDetail.as_view()),
    path('marmitas/<int:pk>/solicitar/', SolicitacaoView.as_view()),
    path('minhas_solicitacoes/', ListaSolicitacaoView.as_view()),
    path('solicitaram_minha_marmita/', PessoasQueSolicitaramMinhaMarmitaView.as_view()),
]