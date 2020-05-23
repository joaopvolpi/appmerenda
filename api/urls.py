from django.urls import path, include
from .views import *
from api import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static 
#router = DefaultRouter()
#router.register('', View)


urlpatterns = [
    #path('', include(router.urls))
    path('naovalidados/', UserList.as_view()),
    path('naovalidados/<int:pk>/', UserDetail.as_view()),
    path('marmitas/', MarmitaList.as_view()),
    path('marmitas/<int:pk>/', MarmitaDetail.as_view()),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
