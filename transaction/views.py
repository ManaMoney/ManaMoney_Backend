from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics, permissions
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.db.models.fields import DateField
from django.db.models.functions import Trunc

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
    filter_fields = ('category_type', 'category_sub_type', 'transaction_type',)
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


# class TransactionFilterView(generics.ListAPIView):
#     serializer_class = serializers.TransactionFilterSerializer 
    # queryset = models.Transaction.objects.all() 
    # queryset = models.Transaction.get_all_expense_monthly(models.Transaction)
    # filter_fields = ('transaction',)  
    # def get_queryset(self):
    #     # filter_transaction = self.request.GET.get('filter', 'INCOME')
    #     filter_date = self.request.GET.get('filter', '')
    #     new_context = models.Transaction.objects.annotate(
    #             date = Trunc(
    #                 'transaction_date', filter_date, output_field= DateField())).values(
    #                     'date')
    #     return new_context

# .filter(transaction = filter_transaction)

# class FilterView(ListView):
    # model = models.Transaction
    # template = None

    # def get_query_set(self):
    #     filter_val = self.request.GET.get('filter', 'INCOME')
    #     new_context = models.Transaction.objects.filter(
    #         transaction = filter_val,
    #     )
    #     return new_context

    # def get_context_data(self, **kwargs):
    #     context = super(FilterView, self).get_context_data(**kwargs)
    #     context['filter'] = self.request.GET.get('filter', 'INCOME')
    #     return context


# class TransactionTotalView(generics.RetrieveAPIView):
#     queryset = models.Transaction.get_total_expense_monthly(models.Transaction)
#     lookup_field = 'transaction'
    # serializer_class
