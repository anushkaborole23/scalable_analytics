# Generated by Django 2.0.13 on 2020-09-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userinformationlayermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformationlayermodel',
            name='da',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userinformationlayermodel',
            name='schemaregistry',
            field=models.CharField(max_length=100),
        ),
    ]
