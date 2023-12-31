# Generated by Django 2.0.13 on 2020-09-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetLayerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unithead', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('shift', models.IntegerField()),
                ('productquantity', models.IntegerField()),
                ('noofworkers', models.IntegerField()),
            ],
            options={
                'db_table': 'AssetTable',
            },
        ),
    ]
