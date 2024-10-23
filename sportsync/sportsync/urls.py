from django.contrib import admin
from django.urls import path, include
from sportsync_app import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('login-email/', views.LoginEmailView.as_view(), name='login-email'),
    path('cadastro/', views.CadastroView.as_view(), name='cadastro'),
    path('dashboard/', login_required(views.DashboardView.as_view()), name='dashboard'),
    path('criarPartidas/', login_required(views.CriarPartidasView.as_view()), name='criarPartidas'),
    path('agendamento/', login_required(views.AgendamentoView.as_view()), name='agendamento')
]
