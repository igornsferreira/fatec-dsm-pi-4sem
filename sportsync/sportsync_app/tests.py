from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Usuario

User = get_user_model()

class UserViewsTest(TestCase):
    
    def setUp(self):
        # Cria um usuário de teste
        self.user = User.objects.create_user(
            email='test@example.com',
            password='TestPassword123!', 
            nome='Test User',
            telefone='(11) 91234-5678'
        )
    
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_email_view_get(self):
        response = self.client.get(reverse('login-email'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login-email.html')

    def test_login_email_view_post_success(self):
        response = self.client.post(reverse('login-email'), {
            'username': 'test@example.com',
            'password': 'TestPassword123!'
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para o dashboard
        self.assertRedirects(response, reverse('dashboard'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_email_view_post_invalid_credentials(self):
        response = self.client.post(reverse('login-email'), {
            'username': 'test@example.com',
            'password': 'WrongPassword!'
        })
        self.assertEqual(response.status_code, 200)  # Retorna ao login
        self.assertContains(response, 'Credenciais inválidas. Tente novamente.')

    def test_login_email_view_post_register(self):
        response = self.client.post(reverse('login-email'), {
            'username': 'newuser@example.com',
            'password': 'NewPassword123!',
            'cadastro_form-0-nome': 'New User',
            'cadastro_form-0-telefone': '(11) 91234-5678',
            'cadastro_form-0-senha': 'NewPassword123!',
            'cadastro_form-0-confirmacao_senha': 'NewPassword123!',
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para o login
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(Usuario.objects.filter(email='newuser@example.com').exists())

    def test_cadastro_view_get(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro.html')

    def test_cadastro_view_post_success(self):
        response = self.client.post(reverse('cadastro'), {
            'nome': 'New User',
            'email': 'newuser@example.com',
            'telefone': '(11) 91234-5678',
            'senha': 'NewPassword123!',
            'confirmacao_senha': 'NewPassword123!',
        })
        self.assertEqual(response.status_code, 302)  # Redireciona para o login
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(Usuario.objects.filter(email='newuser@example.com').exists())

    def test_dashboard_view(self):
        self.client.login(email='test@example.com', password='TestPassword123!')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_criar_partidas_view(self):
        self.client.login(username='test@example.com', password='TestPassword123!')
        response = self.client.get(reverse('criarPartidas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'criarPartidas.html')

    def test_agendamento_view(self):
        self.client.login(username='test@example.com', password='TestPassword123!')
        response = self.client.get(reverse('agendamento'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agendamento.html')
