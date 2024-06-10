# Generated by Django 5.0.1 on 2024-01-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_reportedjoke_alter_joke_from_user_alter_joke_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReportedJoke',
        ),
        migrations.AlterField(
            model_name='joke',
            name='from_user',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='joke',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
