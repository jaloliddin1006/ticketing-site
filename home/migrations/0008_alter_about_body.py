# Generated by Django 4.2.11 on 2024-05-06 22:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_ticket_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
