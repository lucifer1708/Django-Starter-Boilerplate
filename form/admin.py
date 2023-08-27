from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Student


# Register your models here.
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("name", "roll_number", "phone_number", "rollnumber_name")
    search_fields = ("name", "roll_number", "phone_number", "rollnumber_name")


admin.site.register(Student, StudentAdmin)
