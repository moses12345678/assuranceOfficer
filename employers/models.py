from django.db import models

import employers
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
    image = models.ImageField(upload_to='images/', blank="true")
    registrationDate = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname


class Traitement(models.Model):
    type_traitement = models.CharField(max_length=500)
    montant_total = models.FloatField(blank=True, null=True)
    montant_a_payer = models.FloatField(blank=True, null=True)
    person = models.ForeignKey(Employers, on_delete=models.CASCADE)

    def __str__(self):
        return self.type_traitement
