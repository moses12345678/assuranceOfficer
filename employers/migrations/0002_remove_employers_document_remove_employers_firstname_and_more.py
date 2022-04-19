# Generated by Django 4.0.4 on 2022-04-18 09:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employers',
            name='document',
        ),
        migrations.RemoveField(
            model_name='employers',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='employers',
            name='lastname',
        ),
        migrations.AddField(
            model_name='employers',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='employers',
            name='image',
            field=models.ImageField(blank='true', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='employers',
            name='matricule',
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='employers',
            name='nom',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employers',
            name='prenom',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employers',
            name='status',
            field=models.CharField(choices=[('Police Nationale/FSSPC', 'Police Nationale/FSSPC'), ('Nationale/DCPAF', 'Nationale/DCPAF')], default='1', max_length=60),
        ),
        migrations.AlterField(
            model_name='employers',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employers',
            name='registrationDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]