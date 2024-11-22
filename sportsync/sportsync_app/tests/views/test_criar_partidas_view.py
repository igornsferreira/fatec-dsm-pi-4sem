from django.test import TestCase
from django.urls import reverse
from ...models import Usuario, Esporte, Quadra, Partida

class CriarPartidasViewTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(
            email="test@example.com",
            password="Senha@123",
            nome="Test User",
            telefone="123456789"
        )
        self.quadra = Quadra.objects.create(nome="Quadra Teste", disponibilidade=True)
        self.esporte = Esporte.objects.create(nome="Futebol")

    def test_criar_partidas_view_get(self):
        self.client.login(email="test@example.com", password="Senha@123")
        response = self.client.get(reverse('criarPartidas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'criarPartidas.html')

    def test_criar_partidas_view_post_valid_data(self):
        self.client.login(email="test@example.com", password="Senha@123")
        response = self.client.post(reverse('criarPartidas'), {
            'quadra_id': self.quadra.id,
            'esporte': self.esporte.id,
            'data': '2024-12-01',
            'hora_inicio': '10:00:00',
            'horario_fim': '12:00:00',
            'max_participantes': 10,
        })
        self.assertRedirects(response, reverse('minhasPartidas'))

    # def test_criar_partidas_view_post_invalid_data(self):
    #     self.client.login(email="test@example.com", password="Senha@123")
    #     response = self.client.post(reverse('criarPartidas'), {
    #         'quadra_id': '',
    #         'esporte': '',
    #         'data': '',
    #         'hora_inicio': '',
    #         'horario_fim': '',
    #         'max_participantes': '',
    #     })
    #     self.assertContains(response, 'Todos os campos devem ser preenchidos.', status_code=200)
