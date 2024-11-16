from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from uuid import UUID

from .models import Quadra, Esporte, Partida
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
            auth_login(request, usuario, backend=backend)
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

        pesquisa = request.GET.get('pesquisa', '')

        if pesquisa:
            try:
                pesquisa_uuid = UUID(pesquisa)
                quadras = quadras.filter(id=pesquisa_uuid)
            except ValueError:
                quadras = quadras.filter(
                    Q(nome__icontains=pesquisa) |  
                    Q(telefone__icontains=pesquisa) |  
                    Q(endereco__rua__icontains=pesquisa) |  
                    Q(endereco__bairro__icontains=pesquisa) |  
                    Q(endereco__cidade__icontains=pesquisa) |  
                    Q(endereco__estado__icontains=pesquisa)  
            )

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
    
class MinhasPartidasView(ListView):
    model = Partida
    template_name = 'minhasPartidas.html'
    context_object_name = 'partidas'

    def get_queryset(self):
        queryset = Partida.objects.filter(organizador=self.request.user)
        
        pesquisa = self.request.GET.get('pesquisa', '')
        
        if pesquisa:
            queryset = queryset.filter(
                Q(id__icontains=pesquisa) |               
                Q(quadra__nome__icontains=pesquisa) |     
                Q(esporte__nome__icontains=pesquisa) |    
                Q(data__icontains=pesquisa) |             
                Q(hora_inicio__icontains=pesquisa) |      
                Q(horario_fim__icontains=pesquisa)        
            )
        
        return queryset
        
    def post(self, request, *args, **kwargs):
        partida_id = request.POST.get('partida_id')
        if partida_id:
            partida = get_object_or_404(Partida, id=partida_id)

            if partida.organizador != request.user and request.user not in partida.usuarios.all():
                return HttpResponseForbidden("Você não tem permissão para excluir esta partida.")

            partida.delete()

        return redirect('minhasPartidas')
    
def LogoutView(request):
    """Faz logout do usuário."""
    logout(request)
    return HttpResponseRedirect(reverse('home'))

class DashboardHomeView(LoginRequiredMixin, View):
    template_name = 'dashboardHome.html'

    def get(self, request):
        return render(request, self.template_name)
    
class EncontrePartidasView(LoginRequiredMixin, View):
    template_name = 'encontrePartidas.html'

    def get(self, request):
        partidas = Partida.objects.all()

        filtrar_curtidas = request.GET.get('curtidas')
        if filtrar_curtidas == 'curtidas':  
            partidas = partidas.filter(curtidas=request.user)

        pesquisa = request.GET.get('pesquisa')
        if pesquisa:
            partidas = partidas.filter(
                Q(organizador__nome__icontains=pesquisa) |
                Q(quadra__nome__icontains=pesquisa) |
                Q(esporte__nome__icontains=pesquisa)
            )

        context = {
            'partidas': partidas.distinct(),  
        }
        return render(request, self.template_name, context)

    def post(self, request, partida_id=None):
        partida = get_object_or_404(Partida, id=partida_id)

        if request.user in partida.curtidas.all():
            partida.curtidas.remove(request.user)
        else:
            partida.curtidas.add(request.user)

        return HttpResponseRedirect(reverse('encontrePartidas'))