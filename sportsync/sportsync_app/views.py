from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Quadra, Esporte, Partida
from django.contrib.auth import login as auth_login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CadastroForm, LoginEmailForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils import timezone

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

class LoginEmailView(LoginView):
    template_name = 'login-email.html'

    def get(self, request):
        form = LoginEmailForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginEmailForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            senha = form.cleaned_data.get('senha')
            user = authenticate(request, email=email, password=senha)

            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')  

            form.add_error(None, 'Credenciais inválidas. Tente novamente.')  

        return render(request, self.template_name, {'form': form})

class CadastroView(View):
    template_name = 'cadastro.html'

    def get(self, request):
        form = CadastroForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CadastroForm(request.POST)

        if form.is_valid():
            usuario = form.save()  
            backend = 'allauth.account.auth_backends.AuthenticationBackend'  
            login(request, usuario, backend=backend)
            return redirect('dashboard') 

        return render(request, self.template_name, {'form': form})

class DashboardView(LoginRequiredMixin, View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)

class CriarPartidasView(LoginRequiredMixin, View):
    template_name = 'criarPartidas.html'

    def get(self, request):
        quadras = Quadra.objects.all()
        esportes = Esporte.objects.all()
        return render(request, self.template_name, {'quadras': quadras, 'esportes': esportes})

    def post(self, request):
        quadra_id = request.POST.get('quadra_id')
        esporte_id = request.POST.get('esporte')
        data = request.POST.get('data')
        hora_inicio = request.POST.get('hora_inicio')
        horario_fim = request.POST.get('horario_fim')
        max_participantes = request.POST.get('max_participantes')

        if not quadra_id or not esporte_id or not data or not hora_inicio or not horario_fim or not max_participantes:
            return render(request, self.template_name, {
                'error': 'Todos os campos devem ser preenchidos.',
                'quadras': Quadra.objects.all(),
                'esportes': Esporte.objects.all(),
            })

        organizador = request.user

        quadra = get_object_or_404(Quadra, id=quadra_id)
        esporte = get_object_or_404(Esporte, id=esporte_id)

        partida = Partida.objects.create(
            organizador=organizador,
            esporte=esporte,
            data=data,
            hora_inicio=hora_inicio,
            horario_fim=horario_fim,
            quadra=quadra,
            max_participantes=max_participantes,
        )

        return redirect('dashboard')

class PerfilView(LoginRequiredMixin, View):
    template_name = 'perfil.html'

    def get(self, request):
        usuario = request.user
        return render(request, self.template_name, {'usuario': usuario})
    
class EditarPerfilView(LoginRequiredMixin, View):
    template_name = 'editarPerfil.html'

    def get(self, request):
        usuario = request.user
        return render(request, self.template_name, {'usuario': usuario})

    def post(self, request):
        usuario = request.user
        
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario.nome = nome
        usuario.telefone = telefone
        usuario.email = email

        if senha:
            usuario.set_password(senha)  

        usuario.save()  
        return redirect('perfil')  
    
def LogoutView(request):
    """Faz logout do usuário."""
    logout(request)
    return HttpResponseRedirect(reverse('home'))