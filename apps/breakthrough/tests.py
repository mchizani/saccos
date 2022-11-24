from django.test import TestCase 
import datetime
from dateutil import relativedelta

print(datetime.datetime(2022, 11, 1))
nextmonth = datetime.date.today() + relativedelta.relativedelta(months=1) + relativedelta.relativedelta(day=31)
print(nextmonth)