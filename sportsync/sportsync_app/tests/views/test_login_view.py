from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginViewTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='TestPassword123!'
        )
    
    def test_login_view(self):
        response = self.client.get(reverse('login-email'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login-email.html')

    def test_login_email_view_get(self):
        response = self.client.get(reverse('login-email'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login-email.html')

    def test_login_email_view_post_success(self):
        response = self.client.post(reverse('login-email'), {
            'email': 'test@example.com',
            'password': 'TestPassword123!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_email_view_post_invalid_credentials(self):
        # Teste com credenciais inválidas
        response = self.client.post(reverse('login-email'), {
            'email': 'test@example.com',
            'password': 'WrongPassword!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Credenciais inválidas. Tente novamente.')
