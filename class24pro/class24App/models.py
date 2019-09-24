from django.db import models
from django.utils import timezone


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.last_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
