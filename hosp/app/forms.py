from django import forms
from django.forms import ModelForm

from .models import SickHistory


class SickHistoryForm(ModelForm):
    date_sickness = forms.DateField(widget=forms.SelectDateWidget)


    def __init__(self, *args, **kwargs):
        patient = kwargs.pop('pat')
        super(SickHistoryForm, self).__init__(*args, **kwargs)
        self.fields['patient'].initial = patient
        print(patient)

    class Meta:
        model = SickHistory
        fields = ['cause', 'date_sickness', 'patient']
        #labels = {'Cēlonis': 'Book title', }
