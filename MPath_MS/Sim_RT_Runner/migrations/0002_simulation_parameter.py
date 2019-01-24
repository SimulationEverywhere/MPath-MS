# Generated by Django 2.0.4 on 2019-01-24 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PMGMP', '0004_pmgbpmodel_parameters'),
        ('Sim_RT_Runner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulation',
            name='parameter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PMGMP.Parameter'),
            preserve_default=False,
        ),
    ]
