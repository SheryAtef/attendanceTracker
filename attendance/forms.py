from django import forms

from .models import Admission
from .models import Person

class AdmissionForm(forms.ModelForm):

    class Meta:
        model = Admission
        fields = ('person', 'lastAttendance',)
