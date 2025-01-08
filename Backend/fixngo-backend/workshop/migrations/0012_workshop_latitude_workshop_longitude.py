# Generated by Django 5.1.3 on 2025-01-05 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0011_workshopservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='workshop',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]