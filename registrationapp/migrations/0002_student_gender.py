# Generated by Django 3.0.8 on 2020-11-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrationapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
