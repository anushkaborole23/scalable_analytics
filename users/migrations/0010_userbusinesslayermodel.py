# Generated by Django 2.0.13 on 2020-09-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_userfunctionallayermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBusinessLayerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anomalyname', models.CharField(max_length=100)),
                ('energyoptimization', models.CharField(max_length=100)),
                ('conditionmonitor', models.CharField(max_length=100)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'BusinessTable',
            },
        ),
    ]
