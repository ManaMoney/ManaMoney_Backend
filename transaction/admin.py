from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'birth_date',
    ]

class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'transaction',
        'amount',
        'content',
        'transaction_date',
        'category',
    ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category_type',
        'category_sub_type',
    ]
    filter_horizontal = ('user',)


admin.site.register(User, UserAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Category, CategoryAdmin)    
