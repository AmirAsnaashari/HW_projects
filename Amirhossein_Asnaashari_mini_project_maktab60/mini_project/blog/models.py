from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    text = models.CharField(max_length=30, unique=True)

class Post(models.Model):
    slug = models.SlugField(unique=True, max_length=20,null = True )
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
class Comment(models.Model):
    text = models.TextField(max_length=200)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)