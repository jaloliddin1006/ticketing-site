# Generated by Django 4.2.11 on 2024-05-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_eventdate_date_alter_eventdate_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdate',
            name='price',
            field=models.IntegerField(default=10000),
        ),
    ]
