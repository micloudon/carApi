from django.contrib import admin

from .models import Car
from import_export.admin import ImportExportModelAdmin

@admin.register(Car)
class ViewAdmin(ImportExportModelAdmin):
    pass
