# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from users.models import UserPlayer
from avatar.models import Avatar
from django.db import models
from django.core.validators import MinLengthValidator


class Iten(models.Model):
    name = models.CharField(max_length=80, validators=[MinLengthValidator(5)],
                            blank=False, verbose_name="Name")
    description = models.TextField(verbose_name="Description", max_length=250,
                                   blank=False)
    avatar = models.ForeignKey(Avatar, null=True, blank=False,
                               verbose_name="Description", on_delete=models.CASCADE)


class PlayerInventory(models.Model):
    player = models.ForeignKey(UserPlayer, on_delete=models.CASCADE,
                               verbose_name="Player")
    itens = models.ManyToManyField(Iten, blank=True, verbose_name="Itens")

    # generate QR code to tickets function
    # def generateQRCode(self):
