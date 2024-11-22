from django.urls import path
from .views import (
    HomeView,
    LoginEmailView,
    CadastroView,
    CriarPartidasView,
    MinhasPartidasView,
    EncontrePartidasView,
    LogoutView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginEmailView.as_view(), name='login_email'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('criar-partidas/', CriarPartidasView.as_view(), name='criarPartidas'),
    path('minhas-partidas/', MinhasPartidasView.as_view(), name='minhasPartidas'),
    path('encontre-partidas/', EncontrePartidasView.as_view(), name='encontrePartidas'),
    path('logout/', LogoutView, name='logout'),
]
