from django.db import models
from shortuuidfield import ShortUUIDField
from django.contrib.auth.models import User
# Create your models here.
choices={  'aborted': 'aborted',
         'completed':'completed'}
class Menu(models.Model):
    mid = ShortUUIDField(unique=True, primary_key=True)
    title= models.CharField(max_length=50 , unique= True, default='untitle Menu')
    image = models.ImageField(upload_to='menu-image')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default="5000")
    promo_price = models.DecimalField(max_digits=9, decimal_places=2, default="350")
    avalable = models.BooleanField(default=True)

    def __str__(self):
        return  self.title
    

class Plats(models.Model):
    pid = ShortUUIDField(unique=True, primary_key=True)
    title= models.CharField(max_length=50 , unique= True, default='untitle plat')
    image = models.ImageField(upload_to='plats-image')
    price = models.DecimalField(max_digits=9, decimal_places=2, default="1000")
    promo_price = models.DecimalField(max_digits=9, decimal_places=2, default="750")
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, default='unset menu' , null=True)
    description = models.TextField(blank=True, null=True)
    avalable = models.BooleanField(default=True)

    def __str__(self):
        return  self.title


class Commande_Menu(models.Model):
    user = models.CharField(max_length=150, null = False)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, default='unset menu' , null=True)
    status = models.CharField( max_length=50, choices=choices)
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return  self.user

class Commande_Plat(models.Model):
    user = models.CharField(max_length=150, null = False)
    plat = models.ForeignKey(Plats, on_delete=models.SET_NULL, default='unset' , null=True)
    status = models.CharField( max_length=50, choices=choices)
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return  self.user

class Pofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_1 =  models.CharField(max_length=150, null = False)
    address_2 =  models.CharField(max_length=150, null = True, default='')
    email = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return  self.user.username