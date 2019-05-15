from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import HttpResponse, JsonResponse

# Create your views here.
from rest_framework.decorators import api_view

from accidents.models import list1, type1, rank1

import logging
logger = logging.getLogger(__name__)

logger.info('------ save_models--------')

@api_view(['GET'])
def accidentslist(request):
    accidents_list = {}
    if request.method =='GET':
        type_code = request.GET.get('type_code','00')
        rank_code = request.GET.get('rank_code','00')
        startdate = request.GET.get('startdate','1900-01-01')
        enddate = request.GET.get('enddate','3099-01-01')
        data = list1.objects.filter(type_code__startswith=type_code, rank_code__startswith=rank_code,
                                    date__gte=startdate,date__lte=enddate)
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
        # accidents_list.append({'page': request.GET.get('page'), 'accidents_total': len(data), 'list': []})
    else:
        accidents_list['page'] = 1
        # accidents_list.append({'page': 1, 'accidents_total': len(data), 'list': []})
    list = []
    for i in range(0, len(accidents_list)):
        for d in data:
            list.append({
                'pk': d.pk,
                'name': d.name,
                'address': d.address,
                'company_code': d.company_code,
                'company_name': d.company_name,
                'item': d.item,
                'type_code': d.type_code,
                'type_name': d.type_name,
                'rank_code': d.rank_code,
                'rank_name': d.rank_name,
                'date': d.date,
                'description': d.description
            })
    accidents_list['accidents_total'] = len(data)
    accidents_list['list'] = list
    # accidents_list['list'] = json.loads(serializers.serialize("json", data))
    # return JsonResponse(accidents_list)
    return JsonResponse(accidents_list, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def accidentdetail(request,pk):
    accident_detail = []
    data = list1.objects.filter(pk = pk)
    accident_detail.append({
        'pk': data[0].pk,
        'name': data[0].name,
        'address': data[0].address,
        'company_code': data[0].company_code,
        'company_name': data[0].company_name,
        'item': data[0].item,
        'type_code': data[0].type_code,
        'type_name': data[0].type_name,
        'rank_code': data[0].rank_code,
        'rank_name': data[0].rank_name,
        'date': data[0].date,
        'description': data[0].description
    })
    return JsonResponse(accident_detail, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['POST']) #新增事故
def addaccident(request):
    if request.method == 'POST':
        if request.POST != '':
            accident = list1()
            accident.name = request.POST.get('name','')
            accident.address = request.POST.get('address','')
            accident.company_code = request.POST.get('company_code','')
            accident.company_name = request.POST.get('company_name','')
            accident.item = request.POST.get('item','')
            accident.type_code = request.POST.get('type_code','')
            accident.type_name = request.POST.get('type_name','')
            accident.rank_code = request.POST.get('rank_code','')
            accident.rank_name = request.POST.get('rank_name','')
            accident.date = request.POST.get('date','')
            accident.description = request.POST.get('description','')
            accident.save()
            return HttpResponse('新增成功！')
        else:
            return HttpResponse('新增失败！')
    else:
        return HttpResponse('新增失败！')


@api_view(['GET']) #查询事故类别
def typeslist(request):
    types_list = []
    if request.method == 'GET':
        data = type1.objects.all()
    for d in data:
        types_list.append({'pk':d.pk,'code':d.code,'name':d.name})
    return JsonResponse(types_list, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])#查询事故级别
def rankslist(request):
    ranks_list = []
    if request.method == 'GET':
        data = rank1.objects.all()
    for d in data:
        ranks_list.append({'pk': d.pk, 'code': d.code, 'name': d.name})
    return JsonResponse(ranks_list, safe=False, json_dumps_params={'ensure_ascii': False})