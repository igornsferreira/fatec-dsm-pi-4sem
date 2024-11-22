from django.test import TestCase
from django.urls import reverse
from ...models import Usuario

class LoginEmailViewTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(
            email="test@example.com",
            password="Senha@123",
            nome="Test User",
            telefone="123456789"
        )

    def test_login_view_get(self):
        response = self.client.get(reverse('login_email'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login-email.html')

    def test_login_view_post_valid_credentials(self):
        response = self.client.post(reverse('login_email'), {
            'email': 'test@example.com',
            'senha': 'Senha@123',
        })
        self.assertRedirects(response, reverse('criarPartidas'))

    def test_login_view_post_invalid_credentials(self):
        response = self.client.post(reverse('login_email'), {
            'email': 'test@example.com',
            'senha': 'WrongPassword',
        })
        self.assertContains(response, 'Credenciais inválidas', status_code=200)
