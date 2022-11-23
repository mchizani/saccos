from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT, DO_NOTHING

# Create your models here.

class accounts(models.Model):
    
    CATEGORY  = (
        ('ASSET', 'Asset'),
        ('PERSON', 'Person'),
        ('CASH', 'Cash'),
    )
    
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE,blank=True, null=True)
    code            = models.CharField('code',max_length=6,blank=True, null=True)
    category        = models.CharField('category',choices=CATEGORY,default='PERSON',max_length=10)
    role            = models.ForeignKey("role", on_delete=DO_NOTHING, blank=True, null=True)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
    
    class Meta:
        db_table = 'de_account'
        managed = True
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'    


class role(models.Model):
    
    title           = models.CharField('role',default='member',max_length=25) 
     
    def __str__(self):
        return 

    def __unicode__(self):
        return 
    
    class Meta:
        db_table = 'de_account_role'
        managed = True
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'    


class transaction_category(models.Model):
    
    parent          = models.ForeignKey('self', blank=True, null=True, related_name='children',on_delete=CASCADE)
    title           = models.CharField('title',max_length=50) 
     
    def __str__(self):
        return 

    def __unicode__(self):
        return 
    
    class Meta:
        db_table = 'de_trx_category'
        managed = True
        verbose_name = 'Transaction Category'
        verbose_name_plural = 'Transaction Categories'    


class payment(models.Model):
    
    # account, status, verification, verified_by, verified_date
      
    STATUS  = (
        ('NEW', 'New'),
        ('VERIFIED', 'Verified'),
    )
    
    account         = models.ForeignKey("accounts", on_delete=DO_NOTHING)
    status          = models.CharField('status',choices=STATUS,default='NEW',max_length=15)
    description     = models.TextField("description")
    
    
    verified_by     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE,blank=True, null=True)
    verified_on     = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    created_on      = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 

    def __unicode__(self):
        return 
    
    class Meta:
        db_table = 'de_payment'
        managed = True
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'    
        
        

class invoice(models.Model):
    # payment, payment category, amount,
    payment         = models.ForeignKey("payment", on_delete=CASCADE)
    category        = models.ForeignKey("transaction_category", on_delete=DO_NOTHING)
    #ref_acc         = 
    amount          = models.FloatField("amount")

    def __str__(self):
        return 

    def __unicode__(self):
        return 
    
    class Meta:
        db_table = 'de_payment_invoice'
        managed = True
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoice'  
        
        
          

class transactions(models.Model):
    
    
    TYPE  = (
        ('CR', 'Credit'),
        ('DR', 'Derbit'),
    )
    
    account         = models.ForeignKey("accounts", on_delete=DO_NOTHING)
    amount          = models.FloatField("amount")
    payment         = models.ForeignKey("payment", related_name="payment_ref", on_delete=CASCADE)
    trx_type        = models.CharField('trx_type',choices=TYPE,default='CR',max_length=7)
    
    created_on      = models.DateTimeField(auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 


    class Meta:
        db_table = 'de_transactions'
        managed = True
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'    