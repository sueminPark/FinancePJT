from rest_framework import serializers
from .models import Exchange


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'
        # 필드 생성 아직
        # pass

