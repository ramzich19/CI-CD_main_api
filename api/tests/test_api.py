from django.test import TestCase
from api.models import Restaurant
from django.urls import reverse
import json
from rest_framework.test import APITestCase
from rest_framework import status
from ..serializers import RestaurantSerializer

class RestaurantTest(APITestCase):

    def setUp(self):
        self.one_restaurant = Restaurant.objects.create(name='Print', address='1')
        Restaurant.objects.create(name='Print12', address='1')

    def test_restaurant(self):
        response = self.client.get(reverse('get_api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        restaurant_serializer_data = RestaurantSerializer(instance=self.one_restaurant).data
        response_data = json.loads(response.content)[0]
        self.assertEqual(restaurant_serializer_data, response_data)

class CreateRestaurantTest(APITestCase):
    def setUp(self):
        self.data = {"name":'Print', "address":'1'}

    def test_restaurant_create(self):
        response = self.client.post(reverse('create_api'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UpdateRestaurantTest(APITestCase):
    def setUp(self):
        self.one_restaurant = Restaurant.objects.create(name='Print', address='1')
        self.data = RestaurantSerializer(self.one_restaurant).data
        self.data.update({'name': 'Changed'})

    def test_can_update_restaurant(self):
        response = self.client.put(reverse('update_api', args=[self.one_restaurant.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteRestaurantTest(APITestCase):
    def setUp(self):
        self.one_restaurant = Restaurant.objects.create(name='Print', address='1')

    def test_can_delete_restaurant(self):
        response = self.client.delete(reverse('delete_api', args=[self.one_restaurant.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)