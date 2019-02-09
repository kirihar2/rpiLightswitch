# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class GPIO(models.Model):
    GPIO_Pin = models.CharField(max_length=200)
    toggle_on = models.BooleanField(default = True)
    pub_date = models.DateTimeField('date published')
