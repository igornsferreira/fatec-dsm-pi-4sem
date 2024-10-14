from django.http import HttpResponse
from django.views import View
from .models import Usuario
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import LoginEmailForm, CadastroForm

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

class LoginEmailView(View):
    template_name = 'login-email.html'

    def get(self, request):
        form = LoginEmailForm()  # Para login
        cadastro_form = CadastroForm()  # Para cadastro
        return render(request, self.template_name, {'form': form, 'cadastro_form': cadastro_form})

    def post(self, request):
        form = LoginEmailForm()  # Inicializa o form de login vazio
        cadastro_form = CadastroForm()  # Inicializa o form de cadastro vazio

        if 'login' in request.POST:  # Verificar se é um login
            form = LoginEmailForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')  # Redirecionar para o dashboard ou home
                else:
                    form.add_error(None, "Login inválido.")
        elif 'cadastro' in request.POST:  # Verificar se é um cadastro
            cadastro_form = CadastroForm(request.POST)
            if cadastro_form.is_valid():
                cadastro_form.save()  # Salva o novo usuário
                return redirect('login')  # Redirecionar para o login após cadastro

        # Renderiza o template com os forms, mantendo os dados e erros
        return render(request, self.template_name, {'form': form, 'cadastro_form': cadastro_form})
    
class CadastroView(View):
    template_name = 'cadastro.html'

    def get(self, request):
        form = CadastroForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
        return render(request, self.template_name, {'form': form})


class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)


class criarPartidasView(View):
    template_name = 'criarPartidas.html'

    def get(self, request):
        return render(request, self.template_name)
