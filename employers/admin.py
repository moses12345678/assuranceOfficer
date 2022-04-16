from django.contrib import admin
from .models import *


# Register your models here.


class EmployersAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email',
                    'phone', 'image', 'registrationDate', 'date_updated')


admin.site.register(Employers, EmployersAdmin)


class TraitementAdmin(admin.ModelAdmin):
    list_display = ('type_traitement', 'montant_total',
                    'montant_a_payer', 'person')


admin.site.register(Traitement, TraitementAdmin)
