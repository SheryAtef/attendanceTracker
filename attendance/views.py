from django.shortcuts import render

def admission_list(request):
    return render(request, 'attendance/admission_list.html', {})
# Create your views here.
