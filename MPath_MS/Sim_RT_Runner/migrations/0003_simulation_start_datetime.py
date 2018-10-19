# Generated by Django 2.0.4 on 2018-10-19 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Sim_RT_Runner', '0002_remove_simulation_start_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation',
            name='start_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
