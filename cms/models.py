from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class Text(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    number = models.IntegerField(blank=True , null=True)
