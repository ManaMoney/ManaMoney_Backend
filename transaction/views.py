from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics
# Create your views here.




class CategoryList(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class TransactionList(generics.ListCreateAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    search_fields = ('category__category_type',)
    filter_fields = ('transaction','amount','category__category_type','transaction_date')
    ordering_fields = ('category__category_type','amount')
    ordering = ('-transaction_date') 


class UserList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
