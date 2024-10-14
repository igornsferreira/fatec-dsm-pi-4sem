from django.test import TestCase
from django.urls import reverse
from sportsync_app.models import Usuario
from django.contrib.auth import get_user_model

User = get_user_model()

class UsuarioTests(TestCase):
    
    def setUp(self):
        # Criação de um usuário para testes de login
        self.usuario = Usuario.objects.create_user(
            email='teste@exemplo.com',
            password='SenhaForte123'
        )

    def test_cadastro_sucesso(self):
        """Testa o fluxo de cadastro com sucesso"""
        url = reverse('cadastro')  # Verifica o nome da URL
        data = {
            'nome': 'Teste Usuário',
            'email': 'usuario@exemplo.com',
            'telefone': '11987654321',
            'senha': 'SenhaForte123',
            'confirmacao_senha': 'SenhaForte123'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Usuario.objects.filter(email='usuario@exemplo.com').exists())
    
    def test_cadastro_erro_senhas_diferentes(self):
        """Testa o erro de senhas que não correspondem"""
        url = reverse('cadastro')
        data = {
            'nome': 'Outro Usuário',
            'email': 'outro@exemplo.com',
            'telefone': '11987654322',
            'senha': 'SenhaForte123',
            'confirmacao_senha': 'OutraSenha123'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Senhas não coincidem')
        self.assertFalse(Usuario.objects.filter(email='outro@exemplo.com').exists())

    def test_login_sucesso(self):
        """Testa o fluxo de login com sucesso"""
        url = reverse('login')  # Verifica o nome da URL
        data = {
            'email': 'teste@exemplo.com',
            'senha': 'SenhaForte123'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redireciona para o dashboard
        self.assertRedirects(response, reverse('dashboard'))

    def test_login_falha(self):
        """Testa falha no login com credenciais inválidas"""
        url = reverse('login')
        data = {
            'email': 'teste@exemplo.com',
            'senha': 'SenhaErrada'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Credenciais inválidas')

