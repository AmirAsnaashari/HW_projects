from django.db import models

class Cart(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    customer = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    
    def __str__(self):
        return f'Your Cart included of these items: {self.product}{self.quantity} and your Total price is: {self.total_price}'
    
class Payment(models.Model):
    customer = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    date = models.DateTimeField()
    
class TransactionReport(models.Model):
    Payment = models.ForeignKey('Payment', on_delete=models.CASCADE)
    customer = models.ForeignKey('user.Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    seller = models.ForeignKey('user.Seller', on_delete=models.CASCADE)
    content = models.TextField()
    
    class Meta:
        ordering = ['content']
        # unique_together = [['customer' , 'cart']]

    def __str__(self):
        return f'{self.content}'
