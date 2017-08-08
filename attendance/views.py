from django.shortcuts import render, get_object_or_404
from .models import Admission
from.models import Person
from django.utils import timezone
from .forms import PersonForm
from django.shortcuts import redirect
import json
from datetime import date
today = date.today()
'''
def admission_list(request):
     admissions = Admission.objects.filter(lastAttendance__lte=timezone.now()).order_by('lastAttendance')
     return render(request, 'attendance/admission_list.html',{'admissions':admissions})
'''

def person_list(request):
     persons = Person.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
     return render(request, 'attendance/person_list.html',{'persons':persons})


def person_detail(request,pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'attendance/person_detail.html', {'person': person})
# Create your views here.

def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.author = request.user
            person.published_date = timezone.now()
            person.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = PersonForm()
    return render(request, 'attendance/person_edit.html', {'form': form})

def person_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.author = request.user
            person.published_date = timezone.now()
            person.save()
            return redirect('person_detail', pk=person.pk)
    else:
        form = PersonForm(instance=person)
    return render(request, 'attendance/person_edit.html', {'form': form})


def getReport(request):
    personNames=[]
    Dates=[]
    report=[]
    persons_data = Person.objects.all()
    admissions_data = Admission.objects.all()

    for person in persons_data:
        personNames.append(person.Name)

    for personName in personNames:
        Dates.append(collectingAttendanceForOnePerson(personName))

    for x , y in zip(personNames,Dates):
        item = {'Name':x , 'Dates':y}
        report.append(item)

    return render(request,'attendance/personNames.html',{'report':report})

def SearchingLists(name,monthlist ):
    for x in monthlist :
        if x.person.Name == name :
            return True
    return False

def collectingAttendanceForOnePerson(personName):
    DatesForAPerson=[]
    janAttendance = Admission.objects.filter(lastAttendance__month='01',lastAttendance__year=today.year)
    febAttendance = Admission.objects.filter(lastAttendance__month='02',lastAttendance__year=today.year)
    marAttendance = Admission.objects.filter(lastAttendance__month='03',lastAttendance__year=today.year)
    aprAttendance = Admission.objects.filter(lastAttendance__month='04',lastAttendance__year=today.year)
    mayAttendance = Admission.objects.filter(lastAttendance__month='05',lastAttendance__year=today.year)
    junAttendance = Admission.objects.filter(lastAttendance__month='06',lastAttendance__year=today.year)
    julAttendance = Admission.objects.filter(lastAttendance__month='07',lastAttendance__year=today.year)
    AugAttendance = Admission.objects.filter(lastAttendance__month='08',lastAttendance__year=today.year)
    sepAttendance = Admission.objects.filter(lastAttendance__month='09',lastAttendance__year=today.year)
    octAttendance = Admission.objects.filter(lastAttendance__month='10',lastAttendance__year=today.year)
    novAttendance = Admission.objects.filter(lastAttendance__month='11',lastAttendance__year=today.year)
    DecAttendance = Admission.objects.filter(lastAttendance__month='12',lastAttendance__year=today.year)

    if SearchingLists(personName,janAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    if SearchingLists(personName,febAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    if SearchingLists(personName,marAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    if SearchingLists(personName,aprAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    if SearchingLists(personName,mayAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    if SearchingLists(personName,junAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    if SearchingLists(personName,julAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    if SearchingLists(personName,AugAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    if SearchingLists(personName,sepAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    if SearchingLists(personName,octAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    if SearchingLists(personName,novAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    if SearchingLists(personName,DecAttendance):
        DatesForAPerson.append("Attended")
    else :
        DatesForAPerson.append("___")

    return DatesForAPerson


    '''for personName in personNames:
         DatesForAPerson=[]
         for admission in admissions_data:
            if personName == admission.person.Name :
                 DatesForAPerson.append(admission.lastAttendance)
                 DatesForAPerson.sort()
         Dates.append(DatesForAPerson)'''
