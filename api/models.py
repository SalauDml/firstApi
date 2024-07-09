from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address= models.TextField()
    phone= models.CharField(max_length=20)
    age= models.PositiveIntegerField(null=True, blank=True,default=16)
    created_at=models.DateTimeField(auto_now_add=True)