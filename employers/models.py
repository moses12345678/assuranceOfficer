from atexit import register
from xml.dom.minidom import Document
from django.db import models


class Employers(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email = models.EmailField()
    #photo = models.CharField(max_length=350)
    phone = models.CharField(max_length=30)
    registrationDate = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname
