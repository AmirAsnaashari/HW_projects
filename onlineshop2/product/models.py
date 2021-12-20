from django.db import models
from django.db.models.deletion import CASCADE

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_type = models.CharField(max_length=50)
    
    # class Meta:
    #         ordering = ['category_name']

    # def __str__(self):
    #     return f'{self.name}'
    
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=10)
    category = models.ForeignKey('Category', on_delete=CASCADE)
    product_description = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.product_name} {self.category} {self.price}'
    
class Favorite(models.Model):
    customer = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    units = models.PositiveIntegerField
    
    def __str__(self):
        return f'{self.customer} favorite list:{self.product}{self.unit}'
    
class Comment(models.Model):
    caption = models.CharField(max_length=72)
    content = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    customer = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['caption']
        # unique_together = [['customer' , 'products']]

    def __str__(self):
        return f'{self.caption}'
