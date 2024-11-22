from django.test import TestCase
from django.urls import reverse

class CadastroViewTest(TestCase):
    def test_cadastro_view_get(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro.html')

    def test_cadastro_view_post_valid_data(self):
        response = self.client.post(reverse('cadastro'), {
            'nome': 'Novo Usuário',
            'email': 'novo@example.com',
            'telefone': '123456789',
            'senha': 'Senha@123',
            'confirmacao_senha': 'Senha@123',
        })
        self.assertRedirects(response, reverse('criarPartidas'))

    def test_cadastro_view_post_invalid_data(self):
        response = self.client.post(reverse('cadastro'), {
            'nome': '',
            'email': 'invalid',
            'telefone': '',
            'senha': '123',
            'confirmacao_senha': '123',
        })
        self.assertContains(response, 'Este campo é obrigatório', status_code=200)
