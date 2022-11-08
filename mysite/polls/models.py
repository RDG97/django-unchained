from django.db import models

# Create your models here.
class polls(models.Model):
    title = models.CharField(max_length=300)
    vote = models.CharField(max_length=300)