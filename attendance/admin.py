from django.contrib import admin
from .models import Person
from .models import Admission
from django.contrib import admin, messages
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.forms import ModelForm
#from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from date_range_filter import DateRangeFilter

class PersonAdmin(admin.ModelAdmin):
    list_display = ('Name', 'mobileNumber', 'published_date')
admin.site.register(Person, PersonAdmin)

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('person','lastAttendance')
    list_filter = ('person', ('lastAttendance',DateRangeFilter) ,)
    class Media:
      js = ['/admin/jsi18n/']
admin.site.register(Admission,AdmissionAdmin)
