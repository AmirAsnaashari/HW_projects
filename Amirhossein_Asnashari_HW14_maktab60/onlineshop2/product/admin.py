from django.contrib import admin
from .models import Category, Product, Favorite, Comment

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Favorite)
admin.site.register(Comment)