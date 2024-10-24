from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class CriarPartidasViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='TestPassword123!'
        )

    def test_criar_partidas_view(self):
        self.client.login(email='test@example.com', password='TestPassword123!')
        response = self.client.get(reverse('criarPartidas'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'criarPartidas.html')
