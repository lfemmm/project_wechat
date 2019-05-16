from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view

from users.models import users

import logging
logger = logging.getLogger(__name__)

logger.info('------ save_models--------')

# @ensure_csrf_cookie
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
    code = request.session.get('code','')
    if code:
        information = []
        data =  users.objects.filter(code__exact=code)
        information.append({
            'pk':data[0].pk,
            'code': data[0].code,
            'name': data[0].name,
            'sex': data[0].sex,
            'birthday': data[0].birthday,
            'company_code': data[0].company_code,
            'company_name': data[0].company_name,
            'position': data[0].position,
            'entrytime': data[0].entrytime,
            'email': data[0].email,
            'telephone': data[0].telephone,
            'password': data[0].password
        })
        return JsonResponse(information, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return HttpResponse('请重新登录！')

@api_view(['POST'])
def updateinformation(request):
    if request.method == 'POST':
        code = request.session.get('code', '')
        if code:
            information = users.objects.get(code__exact=code)
            information.code = request.POST.get('code',information.code)
            information.name = request.POST.get('name',information.name)
            information.sex = request.POST.get('sex',information.sex)
            information.birthday = request.POST.get('birthday',information.birthday)
            information.company_code = request.POST.get('company_code',information.company_code)
            information.company_name = request.POST.get('company_name',information.company_name)
            information.position = request.POST.get('position',information.position)
            information.entrytime = request.POST.get('entrytime',information.entrytime)                 #入职时间
            information.email = request.POST.get('email',information.email)
            information.telephone = request.POST.get('telephone',information.telephone)
            information.password = request.POST.get('password',information.password)
            information.save()
            request.session.flush()
            return HttpResponse('更新成功,请重新登录！')
        else:
            return HttpResponse('请先登录')