from django.test import TestCase
from ...models import Usuario

class UsuarioModelTest(TestCase):
    def test_create_user(self):
        user = Usuario.objects.create_user(email="user@example.com", password="Senha@123", nome="User", telefone="123456789")
        self.assertEqual(user.email, "user@example.com")
        self.assertTrue(user.check_password("Senha@123"))

    def test_create_superuser(self):
        superuser = Usuario.objects.create_superuser(email="admin@example.com", password="Senha@123", nome="Admin", telefone="987654321")
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
