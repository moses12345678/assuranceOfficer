# Generated by Django 4.0.4 on 2022-04-11 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0002_remove_employers_document_alter_employers_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employers',
            name='registrationDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]