from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
from rest_framework.decorators import api_view

from accidents.models import list1, type1
from company.models import company
from events.models import list2, type2

import logging
logger = logging.getLogger(__name__)

logger.info('------ save_models--------')

@api_view(['GET'])  #传开始时间、结束时间、事故单位，统计各类别事故
def accident_echart(request):
    startdate = request.GET.get('startdate','1900-01-01')
    enddate = request.GET.get('enddate','2099-12-30')
    companycode = request.GET.get('companycode','00')
    if companycode == '':
        companycode = '00'
    data = {}
    pie = []
    bar = []
    accidents = list1.objects.filter(company_code__startswith =companycode,date__gte=startdate,date__lte=enddate).order_by('type_code')
    companys = company.objects.filter(Q(parentID__code__exact=companycode) | Q(code__exact=companycode))
    types = type1.objects.all()
    typelists = []
    company_names = []
    for t in types:
        typelists.append(t.name)
    # for a in accidents:
    #     typelists.append(a.type_name)
    for c in companys:
        company_names.append(c.name)
    # typelists = list(set(typelists))
    for t in typelists:
        type_code = type1.objects.get(name__exact=t).code
        count = accidents.filter(type_name__exact=t,company_code__startswith =companycode,date__gte=startdate,date__lte=enddate).count()
        if count == 0:
            pass
        else:
            pie.append({'type_code': type_code, 'type_name': t, 'count': count})
    for c in company_names:
        company_code = companys.get(name__exact=c).code
        count = accidents.filter(company_code__startswith=company_code,date__gte=startdate, date__lte=enddate).count()
        if count == 0:
            pass
        else:
            bar.append({'company_code':company_code,'company_name':c,'count':count})
    data['pie_count'] = pie
    data['bar_count'] = bar
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def event_echart(request):
    startdate = request.GET.get('startdate', '1900-01-01')
    enddate = request.GET.get('enddate', '2099-12-30')
    companycode = request.GET.get('companycode', '00')
    if companycode == '':
        companycode = '00'
    data = {}
    pie = []
    bar = []
    events = list2.objects.filter(company_code__startswith=companycode,date__gte=startdate,date__lte=enddate).order_by('type_code')
    companys = company.objects.filter(Q(parentID__code__exact=companycode) | Q(code__exact=companycode))
    types = type2.objects.all()
    typelists = []
    company_names = []
    for t in types:
        typelists.append(t.name)
    # for e in events:
    #     typelists.append(e.type_name)
    for c in companys:
        company_names.append(c.name)
    # typelists = list(set(typelists))
    for t in typelists:
        type_code = type2.objects.get(name__exact=t).code
        count = events.filter(type_name__exact=t,company_code__startswith=companycode,date__gte=startdate,date__lte=enddate).count()
        if count == 0:
            pass
        else:
            pie.append({'type_code': type_code, 'type_name': t, 'count': count})
    for c in company_names:
        company_code = companys.get(name__exact=c).code
        count = events.filter(company_code__startswith=company_code,date__gte=startdate, date__lte=enddate).count()
        if count == 0:
            pass
        else:
            bar.append({'company_code': company_code, 'company_name': c, 'count': count})
    data['pie_count'] = pie
    data['bar_count'] = bar
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
