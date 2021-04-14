from django.contrib import admin
from mysite.models import Contact
from import_export.admin import ImportExportModelAdmin
#from models import person
#from .models import person

# Register your models here.
admin.site.register(Contact)
'''@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display=('name','email','location')
'''
