from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.utils import json

from accidents.models import lists


@api_view(['GET'])
def accidentslist(request):
    accidents_list = {}
    if request.method =='GET':
        data = lists.objects.all()
        paginator = Paginator(data, 10)
        page = request.GET.get('page')
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            data = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            data = paginator.page(paginator.num_pages)
    if request.GET.get('page'):
        accidents_list['page'] = request.GET.get('page')
    else:
        accidents_list['page'] = 1
    total = lists.objects.all().count()
    accidents_list['accidents_total'] = total
    accidents_list['list'] = json.loads(serializers.serialize("json", data))
    return JsonResponse(accidents_list)

@api_view(['GET'])
def accidentdetail(request,id):
    accident_detail = {}
    data = lists.objects.filter(pk = id)
    accident_detail['list'] = json.loads(serializers.serialize("json", data))
    return JsonResponse(accident_detail)


def addaccident(request):
    return None