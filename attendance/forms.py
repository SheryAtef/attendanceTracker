from django import forms

from .models import Admission
from .models import Person

class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('author','Name', 'mobileNumber','published_date',)
