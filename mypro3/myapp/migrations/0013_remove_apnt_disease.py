# Generated by Django 2.0.7 on 2018-08-08 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_apnt_disease'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apnt',
            name='disease',
        ),
    ]