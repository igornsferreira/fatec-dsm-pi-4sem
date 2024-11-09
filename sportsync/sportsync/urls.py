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
    path('perfil/', login_required(views.PerfilView.as_view()), name='perfil'),
    path('editarPerfil/', login_required(views.EditarPerfilView.as_view()), name='editarPerfil'),
    path('minhasPartidas/', login_required(views.MinhasPartidasView.as_view()), name='minhasPartidas'),
    path('dashboardHome/', login_required(views.DashboardHomeView.as_view()), name='dashboardHome'),
    path('logout/', login_required(views.LogoutView), name='logout')
]
