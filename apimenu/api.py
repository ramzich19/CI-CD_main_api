from rest_framework import generics
from rest_framework.response import Response
from .serializers import PizzaSerializer
from .models import Pizza

class PizzaCreateApi(generics.CreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class PizzaApi(generics.ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class PizzaUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class PizzaDeleteApi(generics.DestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer