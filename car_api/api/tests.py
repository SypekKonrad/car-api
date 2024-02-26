from django.test import TestCase
from rest_framework.test import APIClient

class CarAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

#todo  czy napisać test dla modelu którego nie ma w bazie?
    def test_create_car(self):
        response = self.client.post('/cars/', {'make': 'Toyota', 'model': 'Prius'})
        self.assertEqual(response.status_code, 201)