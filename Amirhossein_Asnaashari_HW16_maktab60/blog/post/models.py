from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField("category_name", max_length=50)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name=("title"))
    slug = models.SlugField()
    bodytext = models.TextField(verbose_name=("message"))
    category = models.ManyToManyField(Category, verbose_name='category of this post')

    post_date = models.DateTimeField(
        auto_now_add=True, verbose_name="post date")


    class Meta:
        verbose_name = ('post')
        verbose_name_plural = ('posts')
        ordering = ['post_date']

    def __str__(self):
        return self.title

    def get_url(self):
        kwargs = {
            'slug': self.slug,
            'year': '%04d' % self.post_date.year,
            'month': '%02d' % self.post_date.month,
            'day': '%02d' % self.post_date.day,
        }

        return reverse('post_detail', kwargs=kwargs)


class Comment(models.Model): 
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    content = models.TextField() 
    comment_date = models.DateTimeField(auto_now_add=True) 

    class Meta: 
        ordering = ('comment_date',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post) 