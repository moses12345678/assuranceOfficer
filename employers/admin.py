from django.contrib import admin
from .models import Employers

# Register your models here.


class EmployersAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email',
                    'phone', 'image', 'registrationDate', 'date_updated')


admin.site.register(Employers, EmployersAdmin)
