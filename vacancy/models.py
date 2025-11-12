from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()   
    
    class Meta: 
        db_table = 'company'
        managed = True

    def __str__(self):
        return self.name  



class Car(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.FloatField()
    image = models.ImageField()

    class Meta: 
        db_table = 'car'
        managed = True


class Renta(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    days = models.IntegerField(default=1) 
    total_price = models.FloatField(default=0) 
    
    class Meta: 
        db_table = 'renta'
        managed = True

        

