from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.utils import json

from company.models import company


@api_view(['GET'])
def companylist(request):
    company_list = {}
    if request.method =='GET':
        data = company.objects.all()
    company_list['list'] = json.loads(serializers.serialize("json", data))
    return JsonResponse(company_list)
