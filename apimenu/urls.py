from django.urls import path
from .api import PizzaCreateApi, PizzaApi, PizzaUpdateApi, PizzaDeleteApi

urlpatterns = [
    path('api',PizzaApi.as_view(), name='get_pizza'),
    path('api/create',PizzaCreateApi.as_view(), name='create_pizza'),
    path('api/<int:pk>',PizzaUpdateApi.as_view(), name='update_pizza'),
    path('api/<int:pk>/delete',PizzaDeleteApi.as_view(), name='delete_pizza'),
]
