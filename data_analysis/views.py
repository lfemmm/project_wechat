
from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.utils import json

from accidents.models import list1, type1
from company.models import company
from data_analysis.models import accident_pie, accident_bar, event_pie, event_bar
from events.models import list2, type2


@api_view(['GET'])  #传开始时间、结束时间、事故单位，统计各类别事故
def accident_echart(request):
    startdate = request.GET.get('startdate','1900-01-01')
    enddate = request.GET.get('enddate','2099-12-30')
    companycode = request.GET.get('companycode','00')
    data = []
#获取饼状图数据
    pie = []
    accidents = type1.objects.all()
    for t in accidents:
        # accidents_pie = accident_pie()
        # accidents_pie.type_name = t.name
        # accidents_pie.count = list1.objects.filter(type_name__exact=t.name, company_code__startswith =companycode,
        #                                            date__gte=startdate,date__lte=enddate).count()
        # pie.append(accidents_pie)
        pie.append({'type_code':t.code,'type_name':t.name,'count':list1.objects.filter(type_name__exact=t.name,
                    company_code__startswith =companycode,date__gte=startdate,date__lte=enddate).count()})
#获取柱状图数据
    bar = []
    companys = company.objects.filter(Q(parentID__code__exact=companycode) | Q(code__exact=companycode))
    for c in companys:
    #     accidents_bar = accident_bar()
    #     accidents_bar.company_name = c.name
    #     print(accidents_bar.company_name)
    #     accidents_bar.count = list1.objects.filter(company_code__startswith=c.code,
    #                                                    date__gte=startdate, date__lte=enddate).count()
    #     bar.append(accidents_bar)
        bar.append({'company_code':c.code,'company_name':c.name,'count':list1.objects.filter(company_code__startswith=
                                                       c.code,date__gte=startdate, date__lte=enddate).count()})
    data.append({'pie_count':pie,'bar_count':bar})
    # data['pie_count'] = json.loads(serializers.serialize("json", pie))
    # data['bar_count'] = json.loads(serializers.serialize("json", bar))
    # return JsonResponse(data)
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

def event_echart(request):
    startdate = request.GET.get('startdate', '1900-01-01')
    enddate = request.GET.get('enddate', '2099-12-30')
    companycode = request.GET.get('companycode', '00')
    data = []
    # 获取饼状图数据
    pie = []
    events = type2.objects.all()
    for t in events:
        # events_pie = event_pie()
        # events_pie.type_name = t.name
        # events_pie.count = list2.objects.filter(type_name__exact=t.name, company_code__startswith=companycode,
        #                                            date__gte=startdate,date__lte=enddate).count()
        # pie.append(events_pie)
        pie.append({'type_code': t.code, 'type_name': t.name, 'count': list2.objects.filter(type_name__exact=t.name,
                    company_code__startswith=companycode,date__gte=startdate,date__lte=enddate).count()})
# 获取柱状图数据
    bar = []
    companys = company.objects.filter(Q(parentID__code__exact=companycode) | Q(code__exact=companycode))
    for c in companys:
        # events_bar = event_bar()
        # events_bar.company_name = c.name
        # events_bar.count = list2.objects.filter(company_code__startswith=c.code,
        #                                            date__gte=startdate, date__lte=enddate).count()
        # bar.append(events_bar)
        bar.append({'company_code': c.code, 'company_name': c.name, 'count': list2.objects.filter(company_code__startswith
                    =c.code,date__gte=startdate, date__lte=enddate).count()})
    data.append({'pie_count': pie, 'bar_count': bar})
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
    # data['pie_count'] = json.loads(serializers.serialize("json", pie))
    # data['bar_count'] = json.loads(serializers.serialize("json", bar))
    # return JsonResponse(data)