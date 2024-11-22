from django.test import TestCase
from ...forms import CadastroForm

class CadastroFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'nome': 'João Silva',
            'email': 'joao@example.com',
            'telefone': '123456789',
            'senha': 'Senha@123',
            'confirmacao_senha': 'Senha@123'
        }
        form = CadastroForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        data = {
            'nome': 'João Silva',
            'email': 'joao',
            'telefone': '123456789',
            'senha': 'Senha@123',
            'confirmacao_senha': 'Senha@123'
        }
        form = CadastroForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
