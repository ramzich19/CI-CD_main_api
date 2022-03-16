# Generated by Django 4.0 on 2022-03-12 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0003_delete_pizza'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.CharField(max_length=50, verbose_name='Пицца')),
                ('cheese', models.CharField(max_length=50, verbose_name='С сыром')),
                ('dough', models.CharField(max_length=50, verbose_name='Тесто')),
                ('ingredient', models.CharField(max_length=50, verbose_name='Секретный ингредиент')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.restaurant')),
            ],
        ),
    ]
