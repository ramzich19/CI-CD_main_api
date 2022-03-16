from django.db import models
from api.models import Restaurant

class Pizza(models.Model):
  restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
  pizza = models.CharField(verbose_name="Пицца", max_length=50)
  cheese = models.CharField(verbose_name="С сыром",max_length=50)
  dough = models.CharField(verbose_name="Тесто",max_length=50)
  ingredient = models.CharField(verbose_name="Секретный ингредиент",max_length=50)

  def __str__(self):
    return self.pizza