# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Userinfo(models.Model):

    uname=models.CharField(max_length=100)

    pwd=models.CharField(max_length=100)

    def __unicode__(self):
        return u'uname:%s'%self.uname

class Address(models.Model):

    aname=models.CharField(max_length=30)

    aphone=models.CharField(max_length=11)
    addr=models.CharField(max_length=100)

    isdefault=models.BooleanField(default=False)

    userinfo=models.ForeignKey(Userinfo)

