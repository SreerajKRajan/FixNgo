# Generated by Django 5.1.3 on 2024-12-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]