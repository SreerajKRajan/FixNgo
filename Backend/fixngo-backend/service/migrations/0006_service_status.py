# Generated by Django 5.1.3 on 2025-01-07 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_remove_service_is_approved_remove_service_workshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available', max_length=15),
        ),
    ]
