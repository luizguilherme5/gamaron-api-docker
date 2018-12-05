from __future__ import unicode_literals
from users.models import UserPlayer
from itens.models import Iten
from django.db import models


class Quest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=80, blank=False)
    description = models.TextField()
    reward_xp = models.IntegerField(blank=False)
    reward_score = models.IntegerField(blank=False)
    reward_iten = models.OneToOneField(Iten, on_delete=models.CASCADE, blank=True)
    url = models.URLField()
    creator = models.ForeignKey(UserPlayer, on_delete=models.CASCADE)


class Journal(models.Model):
    status = models.BooleanField()
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    player = models.ForeignKey(UserPlayer, on_delete=models.CASCADE)
    datetime_beg = models.DateTimeField(auto_now_add=True)
    datetime_end = models.DateTimeField(auto_now=True)


class Post(models.Model):
    owner = models.ForeignKey(UserPlayer, on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
