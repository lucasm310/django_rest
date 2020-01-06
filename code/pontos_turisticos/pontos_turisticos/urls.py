from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from django.conf import settings
# from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from core.api.viewsets import PontosTuristicosViewSet
from atracoes.api.viewsets import AtracoesViewSet
from enderecos.api.viewsets import EnderecosViewSet
from comentarios.api.viewsets import ComentariosViewSet
from avaliacoes.api.viewsets import AvaliacoesViewSet
from users.api.viewsets import UserViewSet


router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontosTuristicosViewSet)
router.register(r'atracoes', AtracoesViewSet)
router.register(r'enderecos', EnderecosViewSet)
router.register(r'comentarios', ComentariosViewSet)
router.register(r'avaliacoes', AvaliacoesViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('login/',obtain_auth_token)
]
