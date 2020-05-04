# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from goods.models import *

class Index(View):
    def get(self,request):
        category_id=int(request.GET.get('category','2'))
        cur_category=Category.objects.filter(id=category_id)[0]
        goodsList=Goods.objects.filter(category=cur_category)
        category=Category.objects.all()

        #翻页功能
        cur_num=int(request.GET.get('page','1'))
        paginator=Paginator(goodsList,8)
        goods=paginator.page(cur_num)

        #显示页码
        begin=cur_num-1
        if begin<1:
            begin=1
        end=begin+2
        if end>paginator.num_pages:
            end=paginator.num_pages
        if end>=3:
            begin=end-2
        pageList=range(begin,end+1)

        return render(request,'index.html',{'goods': goods,'category': category,'category_id': category_id,'cur_num': cur_num,'pageList': pageList})


def recommed(func):
    def wrapper(goodsdetail,request,goods_id,*args,**kwargs):

        ck=request.COOKIES.get('recommed','')

        goodsIdList=[gid for gid in ck.split() if gid.strip()]


        goodsObjList=[Goods.objects.filter(id=gid)[0] for gid in goodsIdList if Goods.objects.filter(id=gid)[0].category_id==Goods.objects.filter(id=goods_id)[0].category_id][:4]

        if goods_id in goodsIdList:
            goodsIdList.remove(goods_id)
        goodsIdList.insert(0,goods_id)

        response=func(goodsdetail,request,goods_id,goodsObjList,*args,**kwargs)
        response.set_cookie('recommed',' '.join(goodsIdList))

        return response

    return wrapper


class Goodsdetail(View):

    @recommed
    def get(self,request,goods_id,goodsObjList=[],*args,**kwargs):

        goods_id=int(goods_id)
        goods=Goods.objects.filter(id=goods_id)[0]
        return render(request,'detail.html',{'goods': goods, 'goodsObjList': goodsObjList})


class Query_num(View):
    def get(self,request):

        num=int(request.GET.get('val','1'))
        goods_id=request.GET.get('goods_id','')
        color_id=request.GET.get('color_id','')
        size_id=request.GET.get('size_id','')
        if Goods.objects.filter(id=goods_id)[0].get_Count(size_id,color_id) > num:
            flag=True
        else:
            flag=False
        return JsonResponse({'flag': flag})