# Generated by Django 4.0.4 on 2022-04-16 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0010_alter_employers_image_traitement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traitement',
            name='montant_a_payer',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='traitement',
            name='montant_total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
