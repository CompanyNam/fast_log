from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

class BookerUser(AbstractBaseUser):
    first_name=models.CharField(max_length=120)
    last_name= models.CharField(max_length=120)
    email= models.EmailField(verbose_name="email", unique=True)
    password= models.CharField(max_length=120)
    last_login= models.DateTimeField(verbose_name='last login',default=timezone.now)
    USERNAME_FIELD = 'email'
    
    # def __str__(self):
    #     return '%s: %s' % (self.first_name, self.last_name)


class DriverUser(AbstractBaseUser):
    first_name= models.CharField(max_length=120)
    last_name= models.CharField(max_length=120)
    email= models.EmailField(verbose_name="email", unique=True)
    password= models.CharField(max_length=120)
    last_login= models.DateTimeField(verbose_name='last login',default=timezone.now)
    car_number= models.CharField(max_length=120,default="12AA123")
    passport_serial= models.CharField(max_length=120,default="AZE12345")
    lat=models.CharField(max_length=120,default="12,345")
    len=models.CharField(max_length=120,default="12,345") 

    USERNAME_FIELD = 'email'


class Order(models.Model):
    booker_user=models.ForeignKey(BookerUser,on_delete=models.CASCADE,related_name="booker_user")
    driver_user=models.ForeignKey(DriverUser,on_delete=models.CASCADE,related_name="driver_user")
    width=models.FloatField()
    height=models.FloatField()
    length=models.FloatField()
    initialPlace=models.CharField(max_length=100)
    endPlace=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    distance=models.CharField(max_length=100)
       



class booking(models.Model):
    
    booker=models.CharField(max_length=100)
    initialPlace=models.CharField(max_length=100)
    endPlace=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    distance=models.CharField(max_length=100)
    objectBooked=models.CharField(max_length=100)

    def __str__(self):
        return self.objectBooked

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.ManyToManyField(booking)

    def __str__(self):
        return '%s: %s' % (self.artist)
# Create your models here.
