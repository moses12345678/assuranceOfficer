from django import forms
from django.forms import ModelForm
from .models import *
import calculation


class EmployerForm(ModelForm):
    class Meta:
        model = Employers
        fields = '__all__'


class TraitementForm(ModelForm):
    montant_total = forms.FloatField()
    montant_a_payer = forms.FloatField(
        widget=calculation.FormulaInput('montant_total*(0.20)'))

    class Meta:
        model = Traitement
        fields = '__all__'
