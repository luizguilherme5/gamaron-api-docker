# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from avatar.models import Avatar

from django.db import models


class UserPlayer(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        xp = models.IntegerField(default=0)
        score = models.IntegerField()
        avatar = models.ManyToManyField(Avatar, blank=False)
