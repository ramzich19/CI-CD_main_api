from django.urls import path
from .api import RestaurantCreateApi, RestaurantApi, RestaurantUpdateApi, RestaurantDeleteApi

urlpatterns = [
    path('api',RestaurantApi.as_view(), name='get_api'),
    path('api/create',RestaurantCreateApi.as_view(), name='create_api'),
    path('api/<int:pk>',RestaurantUpdateApi.as_view(),name='update_api'),
    path('api/<int:pk>/delete',RestaurantDeleteApi.as_view(), name='delete_api'),
]
