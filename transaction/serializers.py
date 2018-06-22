from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    user_name = serializers.SlugRelatedField(
        source = 'user',
        many = True,
        read_only = True,
        slug_field= 'username',
    )
    class Meta:
        model = Category
        fields = [
            'id',
            'category_type',
            'category_sub_type',
            'user',
            'user_name',
        ]

        extra_kwargs = {
            'user': { 'write_only': True },
        }

class TransactionSerializer(serializers.ModelSerializer):
    user_name = serializers.SlugRelatedField(
        source = 'user',
        many = False,
        read_only = True,
        slug_field='username',
    )
    category_name = serializers.SlugRelatedField(
        source = 'category',
        many = False,
        read_only=True,
        slug_field='category_type'
    )
    sub_category_name = serializers.SlugRelatedField(
        source = 'category',
        many= False,
        read_only = True,
        slug_field='category_sub_type'
    )
    
    class Meta:
        model = Transaction
        fields = [
            'id',
            'user',
            'user_name',
            'transaction',
            'category',
            'category_name',
            # 'sub_category',
            'sub_category_name',
            'amount','remark',
            'transaction_date'
            ]

    extra_kwargs = {
        'user' : {'write_only': True},
        'category':{ 'write_only':True },
        'sub_category':{ 'write_only':True },

    }


