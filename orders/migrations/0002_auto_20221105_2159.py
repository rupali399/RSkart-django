# Generated by Django 3.1 on 2022-11-05 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='completed_at',
            new_name='created_at',
        ),
    ]
