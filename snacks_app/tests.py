from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class AppTest(TestCase):
    
    def test_snack_list_status(self):
        url = reverse('Snacks')
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_template(self):
        url = reverse('Snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')    

