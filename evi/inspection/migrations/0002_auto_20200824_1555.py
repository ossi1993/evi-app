# Generated by Django 3.1 on 2020-08-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectiontemplateattribute',
            name='txtValueMax',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='inspectiontemplateattribute',
            name='txtValueMin',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='inspectiontemplateattribute',
            name='txtValueTolerance',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
