# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    def __unicode__(self):
        return self.name
