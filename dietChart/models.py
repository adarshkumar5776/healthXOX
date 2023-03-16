from django.db import models

# Create your models here.
class info(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    weight=models.IntegerField()
    height=models.IntegerField()
    gender=models.CharField(max_length=50)
    lmg=models.CharField(max_length=50)
    goal=models.IntegerField()
    active=models.CharField(max_length=50)
    protien=models.IntegerField()
    fat=models.IntegerField()
    carbs=models.IntegerField(null=True)

class diet(models.Model):
    Days=models.CharField(max_length=1000)
    Breakfast=models.CharField(max_length=1000)
    Lunch=models.CharField(max_length=1000)
    Snacks=models.CharField(max_length=1000)
    Dinner=models.CharField(max_length=1000)

class diet1(models.Model):
    Days=models.CharField(max_length=1000)
    Breakfast=models.CharField(max_length=1000)
    Lunch=models.CharField(max_length=1000)
    Snacks=models.CharField(max_length=1000)
    Dinner=models.CharField(max_length=1000)
    
class FoodTracker(models.Model):
    Foods=models.CharField(max_length=1000,null=True)
    Carbs=models.DecimalField(max_digits=5, decimal_places=3,null=True)
    Fat=models.DecimalField(max_digits=5, decimal_places=3,null=True)
    Protien=models.DecimalField(max_digits=5, decimal_places=3,null=True)
    