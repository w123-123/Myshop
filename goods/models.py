# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    cname=models.CharField(max_length=10)

    def __unicode__(self):

        return u'Category:%s'%self.cname

class Goods(models.Model):
    gname=models.CharField(max_length=100)

    gdesc=models.CharField(max_length=100)

    oldprice=models.DecimalField(max_digits=5,decimal_places=2)

    price=models.DecimalField(max_digits=5,decimal_places=2)

    category=models.ForeignKey(Category)

    def __unicode__(self):

        return u'Goods:%s'%self.gname

    def get_Img(self):

        return self.inventory_set.all()[0].color.colorurl

    def get_Color(self):

        color=[]
        for inv in self.inventory_set.all():
            if inv.color not in color:
                color.append(inv.color)

        return color

    def get_Count(self,size_id,color_id):

        return int(self.inventory_set.filter(size_id=size_id,color_id=color_id)[0].count)

    def get_Size(self):

        size=[]
        for inv in self.inventory_set.all():
            if inv.size not in size:
                size.append(inv.size)

        return size

    def get_data(self):

        import collections
        data=collections.OrderedDict()

        for detail in self.goodsdetail_set.all():
            if not data.has_key(detail.gdname):
                data[detail.gdname] = []

            data[detail.gdname].append(detail.gdurl)

        return data


class Color(models.Model):
    colorname=models.CharField(max_length=10)

    colorurl=models.CharField(max_length=100)

    def __unicode__(self):

        return u'Color:%s'%self.colorname

class Size(models.Model):
    sname=models.CharField(max_length=10)

    def __unicode__(self):

        return u'Size:%s'%self.sname

class Inventory(models.Model):
    count=models.PositiveIntegerField()

    color=models.ForeignKey(Color)

    goods=models.ForeignKey(Goods)

    size=models.ForeignKey(Size)

    def __unicode__(self):

        return u'Inventory:%d'%self.count




class GoodsDetailName(models.Model):

    gdname=models.CharField(max_length=30)

class GoodsDetail(models.Model):

    gdurl=models.CharField(max_length=100)

    gdname=models.ForeignKey(GoodsDetailName)

    goods=models.ForeignKey(Goods)