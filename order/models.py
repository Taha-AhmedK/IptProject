from django.db import models
from django.contrib.auth.models import AbstractUser
import json
# Create your models here.



class Category(models.Model):
    Name = models.CharField(max_length=25, blank=False)
    photo = models.ImageField(upload_to='category_pics')


    def __str__(self):
        return f"Category:{self.Name}"

class Dish(models.Model):
    Name = models.CharField(max_length=50,blank=False)
    Details = models.CharField(max_length=9999,blank=False,default="")
    Price = models.IntegerField(blank=False,default=0)
    Modified = models.DateTimeField(auto_now=True)
    Tags = models.ManyToManyField(Category, related_name='recipes', blank=True)
    Slug = models.SlugField()

    def __str__(self):
        return f"Dish:{self.Name}"

class DishImage(models.Model):
    recipe = models.ForeignKey(Dish, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipe_pics')

class User(AbstractUser):
    Tray_Items = models.ManyToManyField(Dish)

class Order(models.Model):
    Dishes = models.ManyToManyField(Dish,related_name='Ordered_In')
    Bill = models.JSONField(encoder=json.JSONEncoder,default=dict)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    Order_By = models.ForeignKey(User,on_delete=models.CASCADE)