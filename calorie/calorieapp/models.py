from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DecimalField
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=CASCADE)
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    options =(
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner'),
        ('snacks','snacks')
    )
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name

class FoodItem(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ManyToManyField(Category)
    carbhohydrate = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    fat = models.DecimalField(decimal_places=2,max_digits=5, default=0)
    protein = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    calorie = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    quantity = models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return self.name

class UserFooditem(models.Model):
    user = models.ManyToManyField(User, blank=True)
    fooditem = models.ManyToManyField(FoodItem)
