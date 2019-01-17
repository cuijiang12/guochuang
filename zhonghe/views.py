from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'index.html')

#关于我们
def about_view(request):
    return render(request, 'about.html')

#新闻资讯
def new_view(request):
    return render(request, 'new.html')

#合作流程
def platform_view(request):
    return render(request, 'platform.html')

#客户服务
def service_view(request):
    return render(request, 'service.html')

#联系我们
def contact_view(request):
    return render(request, 'contact.html')

#一般情况下企业得不到政策资助的主要原因
def newsite_view(request):
    return render(request, 'newsite.html')

#如何成功申请政府扶持资金
def newsite2_view(request):
    return render(request, 'newsite2.html')