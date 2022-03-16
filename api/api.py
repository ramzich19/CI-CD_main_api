from rest_framework import generics
from rest_framework.response import Response
from .serializers import RestaurantSerializer
from .models import Restaurant

class RestaurantCreateApi(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantApi(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDeleteApi(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


