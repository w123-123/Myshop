# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from userapp.models import *
from utils import code


class Login(View):

    def get(self,request):

        return render(request,'login.html')

    def post(self,request):

        uname=request.POST.get('account','')
        pwd=request.POST.get('password','')
        flag=Userinfo.objects.filter(uname=uname)

        if flag:
            if flag[0].pwd==pwd:
                request.session['user']=uname
                return HttpResponseRedirect('/user/center/')
            else:
                return HttpResponse('失败')
        else:
            return HttpResponse('用户不存在')


class LoadCode(View):
    def get(self,request):
        img,txt=code.gene_code()
        request.session['codeText']=txt

        return HttpResponse(img,content_type='image/png')


class CheckCode(View):
    def get(self,request):
        code=request.GET.get('code','')
        if code==request.session['codeText']:
            cflag=True
        else:
            cflag=False

        return JsonResponse({'cflag':cflag})


class Register(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        uname=request.POST.get('account','')
        pwd=request.POST.get('password','')
        if Userinfo.objects.create(uname=uname,pwd=pwd):
            request.session['user']=uname

            return HttpResponseRedirect('/user/center/')
        return HttpResponseRedirect('/user/register/')

class CheckUser(View):

    def get(self,request):

        uname=request.GET.get('uname','')
        if Userinfo.objects.filter(uname=uname):
            return JsonResponse({'flag':True})
        return JsonResponse({'flag':False})


class Center(View):
    def get(self,request):

        return render(request,'center.html')


class Out_login(View):
    def post(self,request):
        request.session.flush()
        if request.session.has_key('user'):
            return JsonResponse({'flag':False})
        return JsonResponse({'flag':True})


class Address_(View):
    def get(self,request):

        return render(request,'address.html')