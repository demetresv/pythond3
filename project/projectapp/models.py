from django.db import models
from django.forms import DateTimeField


class Article (models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    views=models.IntegerField(default=0)
    is_published=models.BooleanField(default=True)
    create_date = models.DateField()
