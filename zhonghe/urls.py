#coding=utf-8
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'gczh/$',views.index_view),
    #关于我们
    url(r'about/$',views.about_view),
    #新闻资讯
    url(r'new/$',views.new_view),
    #合作流程
    url(r'platform/$',views.platform_view),
    #客户服务
    url(r'service/$',views.service_view),
    #联系我们
    url(r'contact/$',views.contact_view),
    #一般情况下企业得不到政策资助的主要原因
    url(r'newsite/$',views.newsite_view),
    #如何成功申请政府扶持资金
    url(r'newsite2/$',views.newsite2_view),
]