from django.db import models
import django

# Create your models here.

class mang(models.Model):
    oige_sona = models.CharField(max_length=200)
    sona1 = models.JSONField(default=["     ", "white"])
    sona2 = models.JSONField(default=["     ", "white"])
    sona3 = models.JSONField(default=["     ", "white"])
    sona4 = models.JSONField(default=["     ", "white"])
    sona5 = models.JSONField(default=["     ", "white"])