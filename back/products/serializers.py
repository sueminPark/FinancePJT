from rest_framework import serializers
from .models import Product


# class ProductListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
#         # 필드 생성 아직
#         # pass


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('users',)

        # 필드 생성 아직
        # fields = 