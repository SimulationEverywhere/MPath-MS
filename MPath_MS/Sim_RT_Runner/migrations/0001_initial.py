# Generated by Django 2.0.4 on 2018-10-19 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PMGMP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(auto_now_add=True)),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('task_id', models.CharField(blank=True, max_length=200, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMGMP.PMGBPModel')),
            ],
        ),
    ]