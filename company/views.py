from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.utils import json

from company.models import company


@api_view(['GET'])
def companylist(request):
    company_list = []
    data = company.objects.all()
    code_2_list = []
    code_4_list = []
    code_6_list = []
    for d in data:
        if len(d.code) == 2:
            code_2_list.append(d.code)
        elif len(d.code) == 4:
            code_4_list.append(d.code)
        else:
            code_6_list.append(d.code)
    for c2 in code_2_list:
        company_list.append({'code': c2, 'name': data.get(code__exact=c2).name, 'children': []})
    for i in range(0, len(company_list)):
        for c4 in code_4_list:
            if c4[0:2] == company_list[i].get('code'):
                company_list[i]['children'].append({'code': c4, 'name': data.get(code__exact=c4).name, 'children': []})
    for i in range(0, len(company_list)):
        for j in range(0, len(company_list[i]['children'])):
            for c6 in code_6_list:
                if c6[0:4] == company_list[i]['children'][j].get('code'):
                    company_list[i]['children'][j]['children'].append(
                        {'code': c6, 'name': data.get(code__exact=c6).name})
    return JsonResponse(company_list, safe=False, json_dumps_params={'ensure_ascii': False})


