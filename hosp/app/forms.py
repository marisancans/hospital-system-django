from django import forms
from django.forms import ModelForm

from .models import SickHistory, Patient, Room


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


class PatientForm(ModelForm):
    care_date_from = forms.DateField(widget=forms.SelectDateWidget)
    care_date_to = forms.DateField(widget=forms.SelectDateWidget)
    current_room = forms.ModelMultipleChoiceField(queryset = Room.objects.all())

    def __init__(self, *args, **kwargs):
        room = kwargs.pop('c_room')
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['current_room'].initial = room


    class Meta:
        model = Patient
        fields = ['name', 'surname', 'p_number', 'address', 'phone', 'care_date_from', 'care_date_to', 'current_room']
        #labels = {'Vārds': 'Uzvārds'}
