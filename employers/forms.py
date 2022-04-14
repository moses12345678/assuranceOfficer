from django.forms import ModelForm
from .models import Employers


class EmployerForm(ModelForm):
    class Meta:
        model = Employers
        fields = '__all__'
