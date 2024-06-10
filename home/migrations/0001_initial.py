# Generated by Django 4.2.1 on 2023-05-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email_address', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=300)),
                ('firstname', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('IPAddr', models.CharField(default='192.168.178.46', max_length=40)),
                ('banned', models.BooleanField(default=False)),
            ],
        ),
    ]