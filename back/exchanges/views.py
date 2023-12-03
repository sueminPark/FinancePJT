from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import requests
from .models import Exchange
from .serializers import ExchangeSerializer
from django.conf import settings


@api_view(['GET'])
def get_exchange(request):
    
    API_URL = settings.EXCHANGE_API_KEY
    
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_URL}&searchdate=20231121&data=AP01'

    response = requests.get(url)
    result = response.json()

    for re in result:
        exchange_data = {
            'cur_unit' : re.get('cur_unit'),
            'cur_nm' : re.get('cur_nm'),
            'deal_bas_r' : re.get('deal_bas_r'),
        }

        if not Exchange.objects.filter(cur_nm=re.get('cur_nm')).exists():
            serializer = ExchangeSerializer(data=exchange_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()


    return Response(result)


@api_view(['GET'])
def cal_exchange(request, selected1, selected2):

    num1 = Exchange.objects.get(cur_nm=selected1).deal_bas_r
    num2 = Exchange.objects.get(cur_nm=selected2).deal_bas_r

    num1 = num1.replace(",", "")
    num2 = num2.replace(",", "")

    result = float(num1) / float(num2)
    
    return Response([{'result' : result}])


