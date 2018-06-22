from django.urls import path
from . import views

urlpatterns = [
    path('user-list/',views.UserListView.as_view(),name = 'user-list'),
    path('user-list/<int:pk>/',views.UserDetailView.as_view()),
    path('category-list/',views.CategoryListView.as_view(),name = 'category-list'),
    path('category-list/<int:pk>',views.CategoryDetailView.as_view()),
    path('transaction-list/',views.TransactionListView.as_view(),name = 'transaction-list'),
    path('transaction-list/<int:pk>',views.TransactionDetailView.as_view()),

]
    