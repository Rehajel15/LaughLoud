# Generated by Django 5.0.1 on 2024-03-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_notification_sended_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sended_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
