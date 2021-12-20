

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.PositiveIntegerField()

class DigitalProduct(Product):
    screen_size = models.PositiveSmallIntegerField()
    os = models.CharField(max_length=100, null=True)

class ElectronicProduct(Product):
    energy = models.PositiveSmallIntegerField()

class Mobile(DigitalProduct):
    camera_resolution = models.PositiveIntegerField()
    sim_cards = models.PositiveIntegerField()

class Laptop(DigitalProduct):
    cpu = models.CharField(max_length=100)
    ram_type = models.CharField(max_length=100)
    

# >>> Product.objects.all() --> all the objects of product
# >>> ElectronicProduct.objects.all() --> electronicproduct objects
# >>> Laptop.objects.all() --> laptop objects

# در این نوع ارث بری ویژگی های مشترک در یک کلاس یا جدول parent گذاشته می شوند و بعد هر کلاس یا جدول child فیلدهای مختص خودش را خواهد داشت که با یک کلید خارجی به کلاس یا جدول parent اشاره می کند. البته توجه کنید که در ORM جنگو این کلید خارجی به صورت فیلد OneToOneField پیاده سازی شده است