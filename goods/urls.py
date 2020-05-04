#coding=utf-8
from django.conf.urls import url

from goods import views

urlpatterns=[
    url(r'^$',views.Index.as_view()),

    url(r'^goodsdetails/(\d+)/$',views.Goodsdetail.as_view()),

    url(r'^query_num/$',views.Query_num.as_view())
]