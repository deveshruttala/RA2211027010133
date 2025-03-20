from django.db import models

class NumberStore(models.Model):
    value = models.IntegerField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)