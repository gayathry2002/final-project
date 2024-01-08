from django.db import models

# Create your models here.
class Card(models.Model):
    image=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    about=models.CharField(max_length=100)


class Testimonials(models.Model):
    paragraph=models.CharField(max_length=500)
    name=models.CharField(max_length=200)


class Contact_us(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=500)


   
