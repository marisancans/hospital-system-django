from django.shortcuts import render

from .models import Patient

def index(request):
    patients = Patient.objects.all()
    context = {'patients': patients, 'med_state_dict': dict(Patient.MED_STATE)}
    return render(request, 'app/index.html', context)

def detail_patient(request, patient_id):
    try:
        p = Patient.objects.get(pk=patient_id)
        p_info_text = ["pacienta id", "vārds", "uzvārds", "personas kods", "adrese", "telefona numurs"]
        p_info_data = [p.patient_id, p.name, p.surname, p.p_number, p.address, p.phone]
        
        p_care_text = ["pieņemšanas datums", "izrakstīšanās datums", "stāvoklis"]
        p_care_data = [p.care_date_from, p.care_date_to, p.medical_state_name()]

        p_info = zip(p_info_text, p_info_data)
        p_care = zip(p_care_text, p_care_data)
    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")
    return render(request, 'patients/detail.html', {'patient': p, 'patient_info': p_info, 'patient_care': p_care})