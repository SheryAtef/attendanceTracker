from django.db import models
from django.utils import timezone
from django.db import models

class Person(models.Model):
    author = models.ForeignKey('auth.User')
    Name = models.CharField(max_length=100)
    mobileNumber= models.BigIntegerField()
    published_date = models.DateField()
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Name


class Admission(models.Model):
     person = models.ForeignKey(Person,on_delete=models.CASCADE,)
     lastAttendance = models.DateField()

     def publish(self):
         self.save()

     def __str__(self):
         return self.person.Name
