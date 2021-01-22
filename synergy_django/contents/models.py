from django.db import models
from django.utils import timezone

class Category(models.Model):
    objects = models.Manager
    category = models.CharField(max_length = 20)

    def __str__(self):
        return self.category

class Book(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length = 30)
    author = models.CharField(max_length = 20)
    publisher = models.CharField(max_length = 10)
    url = models.URLField()

    def __str__(self):
        return self.title

class Content(models.Model):
    objects = models.Manager()
    source = models.ForeignKey("Book", related_name='book', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)
    keyword = models.CharField(max_length = 30, blank=True, null=True)
    key_line = models.CharField(max_length = 100, null=True)   ## All 페이지에 보여지는 핵심 문장
    body = models.TextField(blank=True, null=True)
    # page = models.CharField(max_length = 10, default="p.")
    tmi = models.TextField(blank=True, null=True)
    footnote = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.keyword
