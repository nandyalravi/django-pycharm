from django.db import models

from django.urls import reverse;
#Create your models here....
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=30)  # single-line-text
    dob = models.DateField()
    marks = models.IntegerField()
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    address = models.TextField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})