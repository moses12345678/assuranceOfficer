# Generated by Django 4.0.4 on 2022-04-15 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0005_alter_employers_registrationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='employers',
            name='matricule',
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='employers',
            name='status',
            field=models.CharField(choices=[('1', 'Police Nationale/FSSPC'), ('2', 'Nationale/DCPAF')], default='1', max_length=23),
        ),
        migrations.AlterField(
            model_name='employers',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]