from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

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
        return render(request, self.template_name)
    
class CadastroView(View):
    template_name = 'cadastro.html'
    
    def get(self, request):
        return render(request, self.template_name)