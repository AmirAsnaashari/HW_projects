from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    
class Category(models.Model):
    txt = models.CharField(max_length=30, unique=True)

class Post(models.Model):
    slug = models.SlugField(unique=True, max_length=20)
    photo = models.ImageField(upload_to='static/media/', blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    status = models.ManyToManyField(Category)
    last_update = models.DateTimeField(default=now, editable=True)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    txt = models.TextField(max_length=200)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)