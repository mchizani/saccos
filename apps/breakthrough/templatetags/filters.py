
from django.template import Library
import datetime
from dateutil import relativedelta


register = Library()

@register.filter(name='range')
def filter_range(start, end):
    return range(start, end)

@register.filter(name='split')
def split(value, arg):
    return value.split(arg)

@register.filter(name='first_installment')
def first_installment(value):
    nextmonth = datetime.date.today() + relativedelta.relativedelta(months=1) + relativedelta.relativedelta(day=31)
    return nextmonth