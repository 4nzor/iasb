
from django.db import models

# Create your models here.
class Text(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    number = models.IntegerField(blank=True , null=True)
