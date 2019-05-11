
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
    data = {}
#获取饼状图数据
    pie = []
    # typelist =[]
    #accidents = list1.objects.all()
    # for a in accidents:
    #     typelist.append(a.type_name)
    # typelist = list(set(typelist))
    # for t in typelist:
    accidents = type1.objects.all()
    for t in accidents:
        accidents_pie = accident_pie()
        # accidents_pie.type_name = t
        accidents_pie.type_name = t.name
        accidents_pie.count = list1.objects.filter(type_name__exact=t.name, company_code__startswith =companycode,
                                                   date__gte=startdate,date__lte=enddate).count()
        pie.append(accidents_pie)

#获取柱状图数据
    # barcompanycode = request.GET.get('companycode','00')
    bar = []
    companys = company.objects.filter(Q(parentID__code__exact=companycode) | Q(code__exact=companycode))
    for c in companys:
        accidents_bar = accident_bar()
        accidents_bar.company_name = c.name
        print(accidents_bar.company_name)
        accidents_bar.count = list1.objects.filter(company_code__startswith=c.code,
                                                       date__gte=startdate, date__lte=enddate).count()
        bar.append(accidents_bar)
    data['pie_count'] = json.loads(serializers.serialize("json", pie))
    data['bar_count'] = json.loads(serializers.serialize("json", bar))
    return JsonResponse(data)


def event_echart(request):
    startdate = request.GET.get('startdate', '1900-01-01')
    enddate = request.GET.get('enddate', '2099-12-30')
    companycode = request.GET.get('companycode', '00')
    data = {}
    # 获取饼状图数据
    pie = []
    # typelist = []
    # events = list2.objects.all()
    # for a in events:
    #     typelist.append(a.type_name)
    # typelist = list(set(typelist))
    # for t in typelist:
    events = type2.objects.all()
    for t in events:
        events_pie = event_pie()
        # events_pie.type_name = t
        events_pie.type_name = t.name
        events_pie.count = list2.objects.filter(type_name__exact=t.name, company_code__startswith=companycode,
                                                   date__gte=startdate,date__lte=enddate).count()
        pie.append(events_pie)

    # 获取柱状图数据
    # barcompanycode = request.GET.get('companycode','00')
    bar = []
    companys = company.objects.filter(Q(parentID__code__exact=companycode) | Q(code__exact=companycode))
    for c in companys:
        events_bar = event_bar()
        events_bar.company_name = c.name
        print(events_bar.company_name)
        events_bar.count = list2.objects.filter(company_code__startswith=c.code,
                                                   date__gte=startdate, date__lte=enddate).count()
        bar.append(events_bar)
    data['pie_count'] = json.loads(serializers.serialize("json", pie))
    data['bar_count'] = json.loads(serializers.serialize("json", bar))
    return JsonResponse(data)