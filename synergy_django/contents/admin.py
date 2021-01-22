from django.contrib import admin
from .models import Content, Book, Category

admin.site.register(Content)
admin.site.register(Book)
admin.site.register(Category)