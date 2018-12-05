# Generated by Django 2.0.4 on 2018-06-26 00:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activity_api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ngoactivity',
            name='prelistNgo',
            field=models.ManyToManyField(blank=True, related_name='prelistNgo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hospitalactivity',
            name='prelist',
            field=models.ManyToManyField(blank=True, related_name='prelist', to=settings.AUTH_USER_MODEL),
        ),
    ]
