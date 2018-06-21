from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.timezone.now import timezone
from django.conf import settings

class User(AbstractUser):
    birth_date = models.DateField("birth date", null = True, blank = True)

    def __str__(self):
        return self.username


class Category(models.Model):

    category_type = models.CharField("type", max_length = 20, blank = False)
    category_sub_type = models.CharField("sub-type", max_length = 20, blank = True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return '%s (%s)' %(self.category_type,self.category_sub_type)


class Transaction(models.Model):
    # CHOICES
    TRANSACTION_CHOICES = (
        ('IN', 'Income'),
        ('EXP', 'Expense'),
    )
    # DATABASE FIELDS
    transaction = models.CharField("transaction", max_length = 10, choices = TRANSACTION_CHOICES)
    amount = models.DecimalField("amount", blank = False, default = 0.00, max_digits=10 ,decimal_places= 2,)
    remark = models.TextField("remark",max_length= 50, blank = True, null = False)
    transaction_date = models.DateTimeField("date", auto_now_add= True)
    category = models.ForeignKey(
        Category,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
         verbose_name = 'category',
    )

    # META CLASS
    class Meta:
        get_latest_by = ['-priority', 'date']
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'

    # TO STRING METHOD
    def __str__(self):
        return '%s %d' % (self.transaction, self.amount)



