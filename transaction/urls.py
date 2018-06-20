from django.urls import path
from . import views

urlpatterns = [
    path('transaction-list/',views.TransactionList.as_view(),name = 'transaction-list'),
    path('user-list/',views.UserList.as_view(),name = 'user-list'),
    path('category-list/',views.CategoryList.as_view(),name = 'category-list'),

    
]