# Generated by Django 3.2.16 on 2023-03-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietChart', '0008_auto_20230313_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtracker',
            name='Carbs',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='foodtracker',
            name='Fat',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='foodtracker',
            name='Protien',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
    ]
