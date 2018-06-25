from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('user-list/', login_required(views.UserListView.as_view()),name = 'user-list'),
    path('user-list/<int:pk>/', login_required(views.UserDetailView.as_view())),

    path('category-list/', login_required(views.CategoryListView.as_view()),name = 'category-list'),
    path('category-list/<int:pk>', login_required(views.CategoryDetailView.as_view())),
    # path('category-list/transaction-type/', views.RetrieveCategoryView.as_view()),

    path('transaction-list/', login_required(views.TransactionListView.as_view()),name = 'transaction-list'),
    path('transaction-list/<int:pk>', login_required(views.TransactionDetailView.as_view())),

]
    