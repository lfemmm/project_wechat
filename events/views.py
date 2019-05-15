from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import HttpResponse, JsonResponse

# Create your views here.
from rest_framework.decorators import api_view

from events.models import list2, type2

import logging
logger = logging.getLogger(__name__)

logger.info('------ save_models--------')

@api_view(['GET'])
def eventslist(request):
    events_list = {}
    if request.method =='GET':
        type_code = request.GET.get('type_code', '00')
        startdate = request.GET.get('startdate', '1900-01-01')
        enddate = request.GET.get('enddate', '3099-01-01')
        data = list2.objects.filter(type_code__startswith=type_code, date__gte=startdate, date__lte=enddate)
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
        # events_list.append({'page': request.GET.get('page'), 'events_total': len(data),'list':[]})
    else:
        events_list['page'] = 1
        # events_list.append({'page':1,'events_total':len(data),'list':[]})
    list = []
    for i in range(0,len(events_list)):
        for d in data:
            list.append({
                'pk':d.pk,
                'name' : d.name,
                'address' : d.address,
                'company_code' : d.company_code,
                'company_name' : d.company_name,
                'type_code' : d.type_code,
                'type_name' : d.type_name,
                'date' : d.date,
                'description' : d.description
            })
    events_list['events_total'] = len(data)
    events_list['list'] = list
    # events_list['list'] = json.loads(serializers.serialize("json", data))
    # return JsonResponse(events_list)
    return JsonResponse(events_list, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def eventdetail(request,pk):
    event_detail = []
    data = list2.objects.filter(pk = pk)
    event_detail.append({
        'pk': data[0].pk,
        'name': data[0].name,
        'address': data[0].address,
        'company_code': data[0].company_code,
        'company_name': data[0].company_name,
        'type_code': data[0].type_code,
        'type_name': data[0].type_name,
        'date': data[0].date,
        'description': data[0].description
    })
    # event_detail['list'] = json.loads(serializers.serialize("json", data))
    return JsonResponse(event_detail, safe=False, json_dumps_params={'ensure_ascii': False})
# @api_view(['GET'])
# def eventdetail(request):
#     event_detail = {}
#     data = list2.objects.filter(pk = request.GET.get('id'))
#     event_detail['list'] = json.loads(serializers.serialize("json", data))
#     return JsonResponse(event_detail)

@api_view(['POST']) #新增事故
def addevent(request):
    if request.method == 'POST':
        if request.POST != '':
            event = list2()
            event.name = request.POST.get('name','')
            event.address = request.POST.get('address','')
            event.company_code = request.POST.get('company_code','')
            event.company_name = request.POST.get('company_name','')
            event.type_code = request.POST.get('type_code','')
            event.type_name = request.POST.get('type_name','')
            event.date = request.POST.get('date','')
            event.description = request.POST.get('description','')
            event.save()
            return HttpResponse('新增成功！')
        else:
            return HttpResponse('新增失败！')
    else:
        return HttpResponse('新增失败！')

@api_view(['GET'])  #查询事件类别
def typeslist(request):
    types_list = []
    if request.method == 'GET':
        data = type2.objects.all()
    for d in data:
        types_list.append({'pk':d.pk,'code':d.code,'name':d.name})
    return JsonResponse(types_list, safe=False, json_dumps_params={'ensure_ascii': False})