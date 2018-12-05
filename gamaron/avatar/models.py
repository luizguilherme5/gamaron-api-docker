# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Avatar(models.Model):
    name = models.CharField(blank=False, max_length=80)
    image = models.ImageField(upload_to='static/avatar_images', )
