from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from unittest.mock import patch
from .models import Car, Rating


class CarsPostTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('requests.get')
    def test_cars_post_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'Results': [{'Make_Name': 'Toyota', 'Model_Name': 'Prius'}]
        }

        response = self.client.post('/cars/', {'make': 'Toyota', 'model': 'Prius'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Car.objects.filter(make='Toyota', model='Prius').exists())

    @patch('requests.get')
    def test_cars_post_failure_nonexistent_car(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'Results': []}

        response = self.client.post('/cars/', {'make': 'FSO', 'model': 'Polonez'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Car.objects.filter(make='FSO', model='Polonez').exists())

    @patch('requests.get')
    def test_cars_post_failure_external_api(self, mock_get):
        mock_get.return_value.status_code = 500

        response = self.client.post('/cars/', {'make': 'Toyota', 'model': 'Prius'})

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)


class RateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_rate_valid_data(self):
        car = Car.objects.create(make='Toyota', model='Prius')
        valid_data = {'car': car.id, 'rating': 5}

        response = self.client.post('/rate/', valid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Rating.objects.filter(car=car.id).exists())

    def test_rate_invalid_data(self):
        invalid_data = {'car': 1}

        response = self.client.post('/rate/', invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('rating', response.data)

