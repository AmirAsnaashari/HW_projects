from django.db import models
from django.db.models.deletion import CASCADE

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50, unique=True)
    user_phone = models.CharField(max_length=11, unique=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    
class Seller(models.Model):
    user = models.ForeignKey('User', on_delete=CASCADE)
    seller_id = models.CharField(max_length=20, unique=True)
    # GENDER_CHOICES = [
    #     ('mal', 'male'),
    #     ('fem', 'female'),
    #     ('noset', ('notset'))
    # ]
    # gender = models.CharField(
    #     max_length=3,
    #     choices=GENDER_CHOICES
    # )
    date_joined = models.DateTimeField(auto_now_add=True)
    
        
class Customer(models.Model):
    user = models.ForeignKey('User', on_delete=CASCADE)
    customer_id = models.CharField(max_length=20, unique=True)
    # GENDER_CHOICES = [
    #     ('mal', 'male'),
    #     ('fem', 'female'),
    #     ('noset', 'notset')
    # ]
    # gender = models.CharField(
    #     max_length=3,
    #     choices=GENDER_CHOICES
    # )
    date_joined = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['user']
        
    def __str__(self):
        return self.user
    

