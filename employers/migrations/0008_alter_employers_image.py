# Generated by Django 4.0.4 on 2022-04-20 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0007_alter_traitement_facture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employers',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
