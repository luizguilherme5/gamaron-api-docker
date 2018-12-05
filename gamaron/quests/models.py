from __future__ import unicode_literals
from users.models import UserPlayer
from itens.models import Iten
from django.db import models


class Quest(models.Model):
    title = models.CharField(max_length=80, blank=False)
    description = models.TextField()
    reward_xp = models.IntegerField(blank=False)
    reward_score = models.IntegerField(blank=False)
    reward_iten = models.OneToOneField(Iten, on_delete=models.CASCADE)
    time_beg = models.DateTimeField()
    time_end = models.DateTimeField()
    url = models.URLField()
    creator = models.ForeignKey(UserPlayer, on_delete=models.CASCADE)


class Journal(models.Model):
    status = models.BooleanField()
    quest = models.OneToOneField(Quest, on_delete=models.CASCADE)
    player = models.ForeignKey(UserPlayer, on_delete=models.CASCADE)