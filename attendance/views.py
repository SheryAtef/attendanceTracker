from django.shortcuts import render
from .models import Admission
from.models import Person
from django.utils import timezone

def admission_list(request):
     admissions = Admission.objects.filter(lastAttendance__lte=timezone.now()).order_by('lastAttendance')
     return render(request, 'attendance/admission_list.html',{'admissions':admissions})
# Create your views here.
