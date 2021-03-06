# Generated by Django 4.0 on 2022-03-12 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza', models.CharField(max_length=50, verbose_name='Пицца')),
                ('cheese', models.CharField(max_length=50, verbose_name='С сыром')),
                ('dough', models.CharField(max_length=50, verbose_name='Тесто')),
                ('ingredient', models.CharField(max_length=50, verbose_name='Секретный ингредиент')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='pizza',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.restaurant'),
        ),
    ]
