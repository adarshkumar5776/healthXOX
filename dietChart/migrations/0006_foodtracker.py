# Generated by Django 3.2.16 on 2023-03-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietChart', '0005_diet1'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.CharField(max_length=1000)),
                ('Foods', models.IntegerField()),
                ('Carbs', models.IntegerField()),
                ('Fat', models.IntegerField()),
                ('Protien', models.IntegerField()),
            ],
        ),
    ]