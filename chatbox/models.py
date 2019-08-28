from django.db import models

# Create your models here.


class StudentDetails(models.Model):

    name = models.CharField(max_length=40)
    image  = models.ImageField(upload_to='pictures/')
    email = models.EmailField()
    Area = models.CharField(max_length=30)
    subject = models.CharField(max_length=200 , null=True)
    content = models.CharField(max_length=500)
    instagram = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=200 , null=True)


