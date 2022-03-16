from django.test import TestCase
from apimenu.models import Pizza
from django.urls import reverse
import json
from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import PizzaSerializer
from api.models import Restaurant

class PizzaTest(APITestCase):
    def setUp(self):
        self.one_restaurant = Restaurant.objects.create(name='Print', address='1')
        Restaurant.objects.create(name='Print12', address='1')
        self.one_pizza = Pizza.objects.create(
            restaurant=self.one_restaurant,
             pizza='Print',
             cheese='Print',
             dough='Print',
             ingredient='cheese')
        Pizza.objects.create(
            restaurant=self.one_restaurant,
             pizza='Print',
             cheese='Print',
             dough='Print',
             ingredient='cheese')

    def test_pizza(self):
        response = self.client.get(reverse('get_pizza'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pizza_serializer_data = PizzaSerializer(instance=self.one_pizza).data
        response_data = json.loads(response.content)[0]
        self.assertEqual(pizza_serializer_data, response_data)

class CreatePizzaTestt(APITestCase):
    def setUp(self):
        Restaurant.objects.create(name='Print12', address='1')
        self.valid = {
            'restaurant': 1,
            'pizza': 'Muffin',
            'cheese': 'Muffin',
            'dough': 'Pamerion',
            'ingredient': 'White'
        }

    def test_restaurant_create(self):
        response = self.client.post(
            reverse('create_pizza'), self.valid)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UpdateRestaurantTest(APITestCase):
    def setUp(self):
        self.one_restaurant = Restaurant.objects.create(name='Print12', address='1')
        self.one_pizza = Pizza.objects.create(
            restaurant=self.one_restaurant,
            pizza='Print',
            cheese='Print',
            dough='Print',
            ingredient='cheese')

        self.data = PizzaSerializer(self.one_pizza).data
        self.data.update({'pizza': 'Changed'})

    def test_can_update_restaurant(self):
        response = self.client.put(reverse('update_pizza', args=[self.one_pizza.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteRestaurantTest(APITestCase):
    def setUp(self):
        self.one_restaurant = Restaurant.objects.create(name='Print12', address='1')
        self.one_pizza = Pizza.objects.create(
            restaurant=self.one_restaurant,
            pizza='Print',
            cheese='Print',
            dough='Print',
            ingredient='cheese')

    def test_can_delete_restaurant(self):
        response = self.client.delete(reverse('delete_pizza', args=[self.one_pizza.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)