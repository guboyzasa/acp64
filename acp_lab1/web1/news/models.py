from django.db import models

# Create your models here.
class newsPost(models.Model):
    title = models.CharField(max_length=150)
    newsContent = models.TextField()
    