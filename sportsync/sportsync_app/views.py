from django.http import HttpResponse
from django.views import View
from .models import Usuario
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CadastroForm, LoginEmailForm

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

            form.add_error(None, 'Email ou senha inválidos.')  

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

class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)

class CriarPartidasView(View):
    template_name = 'criarPartidas.html'

    def get(self, request):
        quadras = [
            {
                'nome': '10 shirt Society',
                'endereco': 'Itapecerica da Serra - SP',
                'bairro': 'Parque Paraíso',
                'telefone': '(19) 98846-6237'
            },
            {
                'nome': 'Quadra XYZ',
                'endereco': 'São Paulo - SP',
                'bairro': 'Centro',
                'telefone': '(11) 91234-5678'
            },
        ]
        return render(request, self.template_name, {'quadras': quadras})

class AgendamentoView(View):
    template_name = 'agendamento.html'

    def get(self, request):
        return render(request, self.template_name)
