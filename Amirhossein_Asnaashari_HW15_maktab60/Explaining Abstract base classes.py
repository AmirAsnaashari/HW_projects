from django.db import models

class Student(models.Model):
    name = models.CharField(max_lenght=30)
    age = models.PositiveIntegerField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_lenght=30)
    age = models.PositiveIntegerField()
    major = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
# we change the upper classes to this lower code:
class Common(models.Model):
    name = models.CharField(max_lenght=30)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Student(Common):
    year = models.PositiveIntegerField()

class Teacher(Common):
    major = models.CharField(max_length=30)