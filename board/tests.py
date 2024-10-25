from django.test import TestCase, Client
from django.urls import reverse

class BoardViewTests(TestCase):
    def test_list_view(self):
        client = Client()
        response = client.get(reverse('board:list'))  # 'board:list'로 URL 호출
        self.assertEqual(response.status_code, 200)
        print(response.content.decode())
