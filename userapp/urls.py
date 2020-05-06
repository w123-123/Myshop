#coding=utf-8
from django.conf.urls import url

from userapp import views

urlpatterns=[
    #加载登录页面
    url(r'^login/$',views.Login.as_view()),
    #加载验证码
    url(r'^loadCode/',views.LoadCode.as_view()),
    #检查验证码是否输入正确
    url(r'^checkcode/$',views.CheckCode.as_view()),
    #加载注册页面
    url(r'^register/$',views.Register.as_view()),
    #检查注册邮箱是否存在
    url(r'^checkUser/$',views.CheckUser.as_view()),

    #用户中心
    url(r'^center/$',views.Center.as_view()),
    #退出登录
    url(r'^out_login/$',views.Out_login.as_view()),
    #地址管理
    url(r'^address/$',views.Address_.as_view())
]