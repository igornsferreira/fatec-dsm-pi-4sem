from django.test import TestCase
from ...models import Usuario, Esporte, Partida, Quadra

class PartidaModelTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            email="organizador@example.com",
            password="Senha@123",
            nome="Organizador",
            telefone="123456789"
        )
        self.esporte = Esporte.objects.create(nome="Futebol")
        self.quadra = Quadra.objects.create(nome="Quadra A", disponibilidade=True)

    def test_create_partida(self):
        partida = Partida.objects.create(
            organizador=self.usuario,
            esporte=self.esporte,
            data="2024-12-01",
            hora_inicio="10:00:00",
            horario_fim="12:00:00",
            quadra=self.quadra,
            max_participantes=10
        )
        self.assertEqual(partida.organizador, self.usuario)
        self.assertEqual(partida.esporte, self.esporte)
        self.assertEqual(partida.quadra, self.quadra)
        self.assertEqual(partida.max_participantes, 10)

    def test_partida_string_representation(self):
        partida = Partida.objects.create(
            organizador=self.usuario,
            esporte=self.esporte,
            data="2024-12-01",
            hora_inicio="10:00:00",
            horario_fim="12:00:00",
            quadra=self.quadra,
            max_participantes=10
        )
        self.assertEqual(
            str(partida),
            "Partida de Futebol em Quadra A no dia 2024-12-01"
        )
