from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline


from .models import *


# Register your models here.




admin.site.register(Member)
admin.site.register(Loans)
admin.site.register(Shares)
admin.site.register(color_group)