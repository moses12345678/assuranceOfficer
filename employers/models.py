from atexit import register
from xml.dom.minidom import Document
from django.db import models
# Create your models here.
choice = (
    ("Police Nationale/FSSPC", "Police Nationale/FSSPC"),
    ("Nationale/DCPAF", "Nationale/DCPAF"),
)


class Employers(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    email = models.EmailField()
    status = models.CharField(max_length=60,
                              choices=choice,
                              default='1'
                              )
    matricule = models.CharField(max_length=350, null=True)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    registrationDate = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname
