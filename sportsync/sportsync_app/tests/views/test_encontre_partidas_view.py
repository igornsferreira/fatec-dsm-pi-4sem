from django.test import TestCase
from django.urls import reverse
from ...models import Usuario, Partida

class EncontrePartidasViewTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(
            email="test@example.com",
            password="Senha@123",
            nome="Test User",
            telefone="123456789"
        )

    def test_encontre_partidas_view_get(self):
        self.client.login(email="test@example.com", password="Senha@123")
        response = self.client.get(reverse('encontrePartidas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'encontrePartidas.html')
