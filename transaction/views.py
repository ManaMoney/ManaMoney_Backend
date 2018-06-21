from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics, permissions
# Create your views here.


class UserListView(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permissions_classes = {
        permissions.IsAuthenticatedOrReadOnly,
    }

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permissions_classes = {
        permissions.IsAuthenticatedOrReadOnly,
    }

class CategoryListView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permissions_classes = {
        permissions.IsAuthenticatedOrReadOnly,
    }
    filter_fields = ('category_type', 'category_sub_type',)
    ordering = ('category_type'),

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permissions_classes = {
        permissions.IsAuthenticatedOrReadOnly,
    }

class TransactionListView(generics.ListCreateAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permissions_classes = {
        permissions.IsAuthenticatedOrReadOnly,
    }
    search_fields = ('category__category_type',)
    filter_fields = ('transaction','amount','category',)
    ordering_fields = ('amount', 'transaction_date',)
    ordering = ('-transaction_date') 


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer
    permissions_classes = {
        permissions.IsAuthenticatedOrReadOnly,
    }

