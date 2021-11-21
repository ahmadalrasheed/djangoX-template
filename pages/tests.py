from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class Tests(TestCase):
    def test_snack_list_response(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)
    def test_snack_create_response(self):
        url = reverse('createsnack')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)
    def test_snack_list_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response , 'pages/home.html')
    def test_snack_create_template(self):
        url = reverse('createsnack')
        response = self.client.get(url)
        self.assertTemplateUsed(response , 'snack_create_view.html')

    