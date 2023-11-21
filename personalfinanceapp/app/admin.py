from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(InvestmentType)
admin.site.register(Institution)
admin.site.register(Portfolio)
admin.site.register(Instrument)
