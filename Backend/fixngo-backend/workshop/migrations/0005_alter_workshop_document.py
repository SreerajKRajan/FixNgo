# Generated by Django 5.1.3 on 2024-12-21 08:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0004_alter_workshop_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='document',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])]),
        ),
    ]
