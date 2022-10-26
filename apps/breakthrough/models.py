from django.db import models
from django.contrib.auth.models import User
import json

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.deletion import CASCADE, PROTECT, DO_NOTHING
from django.contrib.postgres.fields import JSONField
from django.urls import reverse
from django.utils.datetime_safe import date
from django.contrib.auth.models import Group
from django.contrib.contenttypes.fields import GenericRelation
import os


# Create your models here.



class Member(models.Model):

    ID_TYPE  = (
        ('NIDA', 'National ID'),
        ('PASSPORT', 'Passport'),
    )
    
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE) 
    color           = models.ForeignKey('color_group', on_delete=DO_NOTHING,blank=True, null=True)
    
    phone_number    = models.CharField('phone_number', max_length=50,default="0700000000")
    id_number       = models.CharField('id_number', max_length=50,default="00000000-00000-000000")
    id_type         = models.CharField('id_type',choices=ID_TYPE,default='NIDA',max_length=10)
    dob             = models.DateField("date_of_birth", default='1900-01-01', auto_now=False, auto_now_add=False)
    city            = models.CharField('city', max_length=50,default='Dar-es-Salaam')
    address         = models.TextField("address",blank=True, null=True)
    
    account_bank    = models.CharField('account_bank', max_length=50,default='NONE')
    account_name    = models.CharField('account_name', max_length=50,default='NONE')
    account_number  = models.CharField('account_number', max_length=50,default='000000000')
    

    def __str__(self):
        return self.user.first_name

    class Meta:
        db_table = 'bt_member'
        managed = True
        verbose_name = 'Member'
        verbose_name_plural = 'Members'    
        

class color_group(models.Model):
    title           = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'bt_color_group'
        managed = True
        verbose_name = 'Color groups'


class Shares(models.Model):
    member          = models.ForeignKey('Member', related_name="member_share", on_delete=CASCADE)
    purchase_date   = models.DateField(auto_now=True)
    purchase_amount = models.IntegerField()
    purchase_ref    = models.CharField(max_length=150)
    verified_by     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    verified_on     = models.DateField(auto_now=True)
    transaction_ref = models.CharField(max_length=150)
    
    def __str__(self):
        return self.purchase_ref

    class Meta:
        db_table = 'bt_shares'
        managed = True
        verbose_name = 'Shares'
        
        
class Loans(models.Model):
    
    STATUS  = (
        ('NEW', 'New'),
        ('CANCELLED', 'Cancelled'),
        ('PROGRESS', 'On Progress'),
        ('COMPLETE', 'Complete'),
    )
    
    member          = models.ForeignKey('Member', related_name="member_loan", on_delete=CASCADE)
    amount          = models.IntegerField()
    request_date    = models.DateTimeField(auto_now=True, auto_now_add=False)
    status          = models.CharField(max_length=14,choices=STATUS,default='NEW')
    verified_by     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    verified_on     = models.DateField(auto_now=True)
    transaction_ref = models.CharField(max_length=150)
    
    def __str__(self):
        return self.member.user.first_name+' '+self.amount
    
    class Meta:
        db_table = 'bt_loans'
        managed = True
        verbose_name = 'Loans'