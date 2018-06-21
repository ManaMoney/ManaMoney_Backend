from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
class TransactionSerializer(serializers.ModelSerializer):
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
        fields = 'transaction','category_name','sub_category_name','amount','remark','transaction_date'

    extra_kwargs = {
        'category':{ 'write_only':True }
    }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'