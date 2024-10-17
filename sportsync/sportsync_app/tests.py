from django.test import TestCase
from django.urls import reverse
from sportsync_app.models import Usuario
from django.contrib.auth import get_user_model

User = get_user_model()

class UsuarioTests(TestCase):
    def setUp(self):
        # Criação de um usuário para testes de login
        self.usuario = Usuario.objects.create(
            email='teste@exemplo.com',
            nome='Teste Usuário',
            telefone='11987654321'
        )
        self.usuario.set_password('SenhaForte123')

    def test_cadastro_sucesso(self):
        """Testa o fluxo de cadastro com sucesso"""
        url = reverse('cadastro')  # Verifica o nome da URL
        data = {
            'nome': 'Teste Usuário',
            'email': 'usuario@exemplo.com',
            'telefone': '11987654321',
            'password': 'SenhaForte123',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Usuario.objects.filter(email='usuario@exemplo.com').exists())
    
    def test_login_sucesso(self):
        """Testa o fluxo de login com sucesso"""
        url = reverse('login')  # Verifica o nome da URL
        data = {
            'email': 'teste@exemplo.com',
            'password': 'SenhaForte123'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redireciona para o dashboard
        self.assertRedirects(response, reverse('dashboard'))

    def test_login_falha(self):
        """Testa falha no login com credenciais inválidas"""
        url = reverse('login')
        data = {
            'email': 'teste@exemplo.com',
            'password': 'SenhaErrada'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Credenciais inválidas')
