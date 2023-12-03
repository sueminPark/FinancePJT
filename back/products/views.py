from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model

import requests
from .models import Product
from .serializers import ProductSerializer

from django.conf import settings

API_URL = settings.FINANCE_API_KEY
@api_view(['GET'])
def get_deposit(request):    
    
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_URL}&topFinGrpNo=020000&pageNo=1'
    
    response = requests.get(url)
    response_result = response.json()['result']

    for i in range(response_result['total_count']):
        data = {'prdt_div': response_result['prdt_div']}
        data.update(response_result['baseList'][i])
        data.update(response_result['optionList'][i])
        if not Product.objects.filter(fin_prdt_nm=data.get('fin_prdt_nm')).exists(): 
            serializer = ProductSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    deposits = Product.objects.filter(prdt_div='D')
    result = ProductSerializer(deposits, many=True)

    return Response(result.data)


@api_view(['GET'])
def get_saving(request):    
      
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_URL}&topFinGrpNo=020000&pageNo=1'
    
    response = requests.get(url)
    response_result = response.json()['result']

    for i in range(response_result['total_count']):
        data = {'prdt_div': response_result['prdt_div']}
        data.update(response_result['baseList'][i])
        data.update(response_result['optionList'][i])
        if not Product.objects.filter(fin_prdt_nm=data.get('fin_prdt_nm')).exists(): 
            serializer = ProductSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    
    savings = Product.objects.filter(prdt_div='S')
    result = ProductSerializer(savings, many=True)

    return Response(result.data)


@api_view(['GET'])
def detail(request, fin_prdt_nm):
    product = Product.objects.get(fin_prdt_nm=fin_prdt_nm)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def get_cart(request,  username):
    
    User = get_user_model()
    
    user = User.objects.get(username=username)
    
    my_products = user.product_set.all()

    serializer = ProductSerializer(my_products, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def cart(request,  username, fin_prdt_nm):
    
    User = get_user_model()
    
    product = Product.objects.get(fin_prdt_nm=fin_prdt_nm)
    user = User.objects.get(username=username)
    
    if user in product.users.all():
        product.users.remove(user)
    else:
        product.users.add(user)

    my_products = user.product_set.all()

    serializer = ProductSerializer(my_products, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_all(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)