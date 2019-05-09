from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.utils import json

from events.models import lists, types


@api_view(['GET'])
def eventslist(request):
    events_list = {}
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
        events_list['page'] = request.GET.get('page')
    else:
        events_list['page'] = 1
    total = lists.objects.all().count()
    events_list['events_total'] = total
    events_list['list'] = json.loads(serializers.serialize("json", data))
    return JsonResponse(events_list)

@api_view(['GET'])
def eventdetail(request,id):
    event_detail = {}
    data = lists.objects.filter(pk = id)
    event_detail['list'] = json.loads(serializers.serialize("json", data))
    return JsonResponse(event_detail)
# @api_view(['GET'])
# def eventdetail(request):
#     event_detail = {}
#     data = lists.objects.filter(pk = request.GET.get('id'))
#     event_detail['list'] = json.loads(serializers.serialize("json", data))
#     return JsonResponse(event_detail)

@api_view(['POST']) #新增事故
def addevent(request):
    if request.method == 'POST':
        if request.POST != '':
            event = lists()
            event.name = request.POST.get('name')
            event.address = request.POST.get('address')
            event.company_code = request.POST.get('company_code')
            event.company_name = request.POST.get('company_name')
            event.type_code = request.POST.get('type_code')
            event.type_name = request.POST.get('type_name')
            event.date = request.POST.get('date')
            event.description = request.POST.get('description')
            event.save()
            return HttpResponse('新增成功！')
        else:
            return HttpResponse('新增失败！')
    else:
        return HttpResponse('新增失败！')

@api_view(['GET'])  #查询事件类别
def typeslist(request):
    types_list = {}
    if request.method == 'GET':
        data = types.objects.all()
    types_list['list'] = json.loads(serializers.serialize("json", data))
    return JsonResponse(types_list)