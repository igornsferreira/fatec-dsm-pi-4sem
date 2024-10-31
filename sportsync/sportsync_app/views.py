from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Quadra
from django.contrib.auth import login as auth_login, logout
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CadastroForm, LoginEmailForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse

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

class CriarPartidasView(View):
    template_name = 'criarPartidas.html'

    def get(self, request):
        quadras = Quadra.objects.all() 
        return render(request, self.template_name, {'quadras': quadras})

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