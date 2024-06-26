# Generated by Django 5.0.1 on 2024-03-13 18:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_profile_isbanned'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.TextField(default='', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
