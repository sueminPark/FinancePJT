from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerizlizer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

User = get_user_model()

@api_view(['GET'])
def detail(request, user_pk):
    user = User.objects.get(pk=user_pk)
    serializer = CustomUserSerizlizer(user)
    return Response(serializer.data)


@api_view(['PUT'])
def update_user(request, user_pk):
    user = User.objects.get(pk=user_pk)

    serializer = CustomUserSerizlizer(user, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
    
    return Response(serializer.data)