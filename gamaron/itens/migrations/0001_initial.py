# Generated by Django 2.0.4 on 2018-12-05 01:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Name')),
                ('description', models.TextField(max_length=250, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itens', models.ManyToManyField(blank=True, to='itens.Iten')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserPlayer')),
            ],
        ),
    ]