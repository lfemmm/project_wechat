from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template.defaulttags import csrf_token
from django.contrib import auth
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view

from users.models import users


@ensure_csrf_cookie
@api_view(['POST'])
def login(request):
    # return JsonResponse(request.POST)
    errors = []
    username = request.POST.get('username')
    password = request.POST.get('password')
    # response = {}
    if request.method == "POST":
        user = users.objects.filter(username__exact=username , password__exact=password)
        if user:
            # response['list'] = json.loads(serializers.serialize("json", user))
            cookie = {}
            # 将username写入浏览器cookie,失效时间为3600
            response = HttpResponse()
            response.set_cookie('username', username, 36000)
            response.set_signed_cookie('username', username, salt='asdasd')  # 带签名的cookie(加盐)
            response.set_cookie('password', password,36000)
            # response['cookie'] = json.loads(serializers.serialize("json", cookie))
            return response
            # return JsonResponse(request.POST)
        else:
            errors.append('用户名或密码错误')
    else:
        pass
    return JsonResponse(request.POST)

@api_view(['POST'])
def logout(request):
    #(1)
    # response = HttpResponse('清除成功')  # 改成重定向等都可以
    # response.delete_cookie('username')
    # response.delete_cookie('password')
    # (2)也可采用重定向
    # return HttpResponseRedirect('/blog')

    auth.logout(request)
    ret = {
        "hhh":"注销啦！！！"
    }
    return JsonResponse(ret)