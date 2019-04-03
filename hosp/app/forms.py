from django import forms
from django.forms import ModelForm

from .models import SickHistory, Patient, Room, MedHistory, Profile
from django.contrib.auth.models import User


class SickHistoryForm(ModelForm):
    date_sickness = forms.DateField(widget=forms.SelectDateWidget)

    def __init__(self, *args, **kwargs):
        patient = kwargs.pop('pat')
        super(SickHistoryForm, self).__init__(*args, **kwargs)
        self.fields['patient'].initial = patient

    class Meta:
        model = SickHistory
        fields = ['cause', 'date_sickness', 'patient']
        #labels = {'Cēlonis': 'Book title', }


class MedHistoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        patient = kwargs.pop('pat')
        super(MedHistoryForm, self).__init__(*args, **kwargs)
        self.fields['patient'].initial = patient

    class Meta:
        model = MedHistory
        fields = ['name', 'price', 'dose', 'patient']
        #labels = {'Cēlonis': 'Book title', }


class PatientForm(ModelForm):
    care_date_from = forms.DateField(widget=forms.SelectDateWidget)
    care_date_to = forms.DateField(widget=forms.SelectDateWidget)
   
    class Meta:
        model = Patient
        fields = ['name', 'surname', 'p_number', 'address', 'phone', 'room', 'care_date_from', 'care_date_to']
        #labels = {'Vārds': 'Uzvārds'}

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "surname", "p_number", "address", "phone"]


