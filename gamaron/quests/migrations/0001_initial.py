# Generated by Django 2.0.4 on 2018-12-05 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itens', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('datetime_beg', models.DateTimeField(auto_now_add=True)),
                ('datetime_end', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserPlayer')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserPlayer')),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('reward_xp', models.IntegerField()),
                ('reward_score', models.IntegerField()),
                ('url', models.URLField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserPlayer')),
                ('reward_iten', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='itens.Iten')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quests.Quest'),
        ),
        migrations.AddField(
            model_name='journal',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quests.Quest'),
        ),
    ]
