# Generated by Django 3.1.7 on 2022-12-28 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='date',
            field=models.DateField(default='1990-01-01'),
            preserve_default=False,
        ),
    ]