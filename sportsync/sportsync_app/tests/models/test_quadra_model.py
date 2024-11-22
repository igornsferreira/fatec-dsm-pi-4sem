from django.test import TestCase
from ...models import Endereco, Quadra, Esporte

class QuadraModelTest(TestCase):
    def setUp(self):
        self.endereco = Endereco.objects.create(
            cep="12345-678",
            rua="Rua Exemplo",
            bairro="Bairro Exemplo",
            numero="123",
            cidade="Cidade Exemplo",
            estado="Estado Exemplo"
        )
        self.esporte = Esporte.objects.create(nome="Basquete")

    def test_create_quadra(self):
        quadra = Quadra.objects.create(
            nome="Quadra Central",
            endereco=self.endereco,
            disponibilidade=True,
            telefone="123456789"
        )
        quadra.esportes.add(self.esporte)

        self.assertEqual(quadra.nome, "Quadra Central")
        self.assertEqual(quadra.endereco, self.endereco)
        self.assertIn(self.esporte, quadra.esportes.all())

    def test_quadra_string_representation(self):
        quadra = Quadra.objects.create(
            nome="Quadra Central",
            endereco=self.endereco,
            disponibilidade=True
        )
        self.assertEqual(str(quadra), "Quadra Central")
