# Generated by Django 5.0.6 on 2024-07-26 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='like',
        ),
    ]
