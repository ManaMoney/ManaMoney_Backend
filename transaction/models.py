from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django.utils.timezone import localdate
from django.db.models import Sum
from django.db.models.fields import DateField
from django.db.models.functions import TruncMonth, TruncYear, Trunc


class User(AbstractUser):
    birth_date = models.DateField("birth date", null = True, blank = True)

    def __str__(self):
        return self.username


class Category(models.Model):

    # CHOICES
    TRANSACTION_TYPE_CHOICES = (
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    )
    # DATABASE FIELDS
    transaction_type = models.CharField("transaction type", max_length = 10, choices = TRANSACTION_TYPE_CHOICES, null = True)
    category_type = models.CharField("type", max_length = 20, blank = False)
    category_sub_type = models.CharField("sub-type", max_length = 20, blank = True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    # META CLASS
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    # TO STRING METHOD
    def __str__(self):
        return '%s (%s)' % (self.category_type,self.category_sub_type)

# class TransactionManager(models.Manager):
#     def get_total_expense(self):
#         total = self.filter(transaction = 'EXPENSE')
#         return total

class Transaction(models.Model):
    # CHOICES
    TRANSACTION_CHOICES = (
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    )
    # DATABASE FIELDS
    user = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        verbose_name = 'user',
        related_name= 'transactions',
        related_query_name= 'transaction',
    )
    transaction = models.CharField("transaction", max_length = 10, choices = TRANSACTION_CHOICES)
    amount = models.DecimalField("amount", blank = False, default = 0.00, max_digits=10 ,decimal_places= 2,)
    content = models.TextField("remark",max_length= 50, blank = True, null = False)
    transaction_date = models.DateTimeField("date",default = timezone.now)
    category = models.ForeignKey(
        Category,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
         verbose_name = 'category',
         related_name= 'transactions',
         related_query_name= 'transaction'
    )
    # objects = TransactionManager()
    
    # META CLASS
    class Meta:
        get_latest_by = '-date'
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'

    # TO STRING METHOD
    def __str__(self):
        return '%s %d' % (self.transaction, self.amount)

    # CUSTOM METHODS
    # def get_total_expense_daily(self):
    #     this_day = localdate()
    #     queryset = self.objects.filter(transaction = 'EXPENSE')
    #     return queryset.annotate(day = Trunc('transaction_date', 'day', output_field = DateField())).filter(day = this_day).aggregate(Sum('amount'))

    # def get_total_income_daily(self):
    #     this_day = localdate()
    #     queryset = self.objects.filter(transaction = 'INCOME')
    #     return queryset.annotate(day = Trunc('transaction_date', 'day', output_field = DateField())).filter(day = this_day).aggregate(Sum('amount'))

    # def get_total_expense_monthly(self):
    #     queryset = self.objects.filter(transaction = 'EXPENSE')
    #     return queryset.annotate(month = TruncMonth('transaction_date')).values('month', 'amount').aggregate(Sum('amount'))

    # def get_all_expense_monthly(self):
    #     queryset = self.objects.filter(transaction = 'EXPENSE')
    #     return queryset.annotate(month = TruncMonth('transaction_date')).values('month', 'amount')

    # def get_total_income_monthly(self):
    #     queryset = self.objects.filter(transaction = 'INCOME')
    #     return queryset.annotate(month = TruncMonth('transaction_date')).values('month', 'amount').aggregate(Sum('amount'))

    # def get_total_expense_yearly(self):
    #     queryset = self.objects.filter(transaction = 'EXPENSE')
    #     return queryset.annotate(month = TruncYear('transaction_date')).values('month', 'amount').aggregate(Sum('amount'))

    # def get_total_income_yearly(self):
    #     queryset = self.objects.filter(transaction = 'INCOME')
    #     return queryset.annotate(month = TruncYear('transaction_date')).values('month', 'amount').aggregate(Sum('amount'))

