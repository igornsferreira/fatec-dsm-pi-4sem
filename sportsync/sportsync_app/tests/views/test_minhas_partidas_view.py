from django.test import TestCase
from django.urls import reverse
from ...models import Usuario, Partida, Esporte

class MinhasPartidasViewTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(
            email="test@example.com",
            password="Senha@123",
            nome="Test User",
            telefone="123456789"
        )
        self.esporte = Esporte.objects.create(nome="Futebol")
        self.partida = Partida.objects.create(
            organizador=self.user,
            # esporte_id=1,
            esporte=self.esporte,
            data="2024-12-01",
            hora_inicio="10:00:00",
            horario_fim="12:00:00",
            max_participantes=10,
        )

    def test_minhas_partidas_view_get(self):
        self.client.login(email="test@example.com", password="Senha@123")
        response = self.client.get(reverse('minhasPartidas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'minhasPartidas.html')
