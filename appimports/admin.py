from django.contrib import admin
from import_export import resources
from .models import Currency
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ForexAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['Date','Dollar','Pound','Euro']

#admin.site.register(SalesData,SalesAdmin)
admin.site.register(Currency,ForexAdmin)

