# Generated by Django 4.1.5 on 2023-01-29 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
                ('size_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('topping_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField(default=False)),
                ('pizza_price', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.size')),
                ('topping', models.ManyToManyField(to='pizza.topping')),
            ],
        ),
    ]
