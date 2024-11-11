from django.test import TestCase
from django.urls import reverse
from sportsync_app.models import Usuario
from django.contrib.auth import get_user_model

User = get_user_model()

class CadastroViewTest(TestCase):
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
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))
        self.assertTrue(Usuario.objects.filter(email='newuser@example.com').exists())

    def test_cadastro_view_post_email_existente(self):
        User.objects.create_user(
            email='existente@teste.com', 
            password='SenhaExistente123!'
        )
        response = self.client.post(reverse('cadastro'), {
            'nome': 'Usuario Existente',
            'email': 'existente@teste.com',
            'telefone': '1234567890',
            'senha': 'SenhaSegura123!',
            'confirmacao_senha': 'SenhaSegura123!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Este email já está em uso.')