# Generated by Django 4.2.7 on 2023-12-02 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_notifications'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notifications',
            new_name='Notification',
        ),
    ]
