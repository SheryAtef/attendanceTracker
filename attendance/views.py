from django.shortcuts import render, get_object_or_404
from .models import Admission
from.models import Person
from django.utils import timezone

def admission_list(request):
     admissions = Admission.objects.filter(lastAttendance__lte=timezone.now()).order_by('lastAttendance')
     return render(request, 'attendance/admission_list.html',{'admissions':admissions})

def person_detail(request,pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'attendance/person_detail.html', {'person': person})     
# Create your views here.
