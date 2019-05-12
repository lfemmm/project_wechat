from django.core import serializers
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.contrib import  messages
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework.utils import json
from users.models import users


@ensure_csrf_cookie
@api_view(['POST'])
def login(request):
    code = request.POST.get('code')
    password = request.POST.get('password')
    # response = {}
    if request.method == "POST":
        user = users.objects.filter(code__exact=code , password__exact=password)
        if user:
            # cookie = {}
            # 将username写入浏览器cookie,失效时间为3600
            # response = HttpResponse()
            # response.set_cookie('code', code, 36000)
            # response.set_signed_cookie('code', code, salt='asdasd')  # 带签名的cookie(加盐)
            # response.set_cookie('password', password,36000)
            request.session['code'] = code
            # response['cookie'] = json.loads(serializers.serialize("json", cookie))
            login = {
                "login_result":"success"
            }
            return JsonResponse(login)
        else:
            login = {
                "login_result": "fail"
            }
            return JsonResponse(login)
    else:
        pass

@api_view(['GET'])
def logout(request):
    #(1)
    # response = HttpResponse('清除成功')  # 改成重定向等都可以
    # response.delete_cookie('username')
    # response.delete_cookie('password')
    # (2)也可采用重定向
    # return HttpResponseRedirect('/blog')
    code = request.session.get('code', '')
    if code:
        request.session.flush()
        logout = {
            "logout_result": "success"
        }
        return JsonResponse(logout)
    else:
        return HttpResponse('请勿重复退出')

@api_view(['GET'])
def userinformation(request):
    #登录时，应用员工编码加密码，不应该使用用户名
    code = request.session.get('code','')
    # code = '201822000366'
    if code:
        information = {}
        information['data'] = json.loads(serializers.serialize("json", users.objects.filter(code__exact=code)))
        # information['data'] = json.loads(str(users.objects.filter(code__exact=code).values('name', 'password')))
        return JsonResponse(information)
    else:
        return HttpResponse('请重新登录！')

@api_view(['POST'])
def updateinformation(request):
    if request.method == 'POST':
        code = request.session.get('code', '')
        if code:
            information = users.objects.get(code__exact=code)
            information.code = request.POST.get('code')
            information.name = request.POST.get('name')
            information.sex = request.POST.get('sex')
            information.birthday = request.POST.get('birthday')
            information.company_code = request.POST.get('company_code')
            information.company_name = request.POST.get('company_name')
            information.position = request.POST.get('position')
            information.entrytime = request.POST.get('entrytime')                 #入职时间
            information.email = request.POST.get('email')
            information.telephone = request.POST.get('telephone')
            information.password = request.POST.get('password')
            information.save()
            request.session.flush()
            return HttpResponse('更新成功,请重新登录！')
        else:
            return HttpResponse('请先登录')