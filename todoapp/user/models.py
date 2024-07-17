from django.db import models

# Create your models here.

class TodoModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    date=models.DateField()
    image=models.ImageField(upload_to="todoimages")
