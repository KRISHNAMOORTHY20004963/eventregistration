from django.db import models
from django.contrib import admin

# Create your models here.


class participant(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    institution=models.CharField(max_length=50)

class participantadmin(admin.ModelAdmin):
    list_display=("username","email","phone","institution")


