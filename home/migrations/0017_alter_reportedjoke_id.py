# Generated by Django 5.0.1 on 2024-01-26 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_reportedjoke_times_reported_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportedjoke',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]