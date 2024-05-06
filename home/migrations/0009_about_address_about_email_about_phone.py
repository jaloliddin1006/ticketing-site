# Generated by Django 4.2.11 on 2024-05-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_about_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]