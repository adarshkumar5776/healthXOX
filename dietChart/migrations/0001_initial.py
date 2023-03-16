# Generated by Django 3.2.16 on 2023-03-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('lmg', models.CharField(max_length=50)),
                ('goal', models.IntegerField()),
                ('active', models.CharField(max_length=50)),
                ('protien', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('carbs', models.IntegerField(null=True)),
            ],
        ),
    ]