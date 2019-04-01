from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.contrib import messages


from app.forms import SickHistoryForm, PatientForm, MedHistoryForm



from .models import Patient, SickHistory, Room, MedHistory

def index(request):
    patients = Patient.objects.all()
    context = {'patients': patients, 'med_state_dict': dict(Patient.MED_STATE)}
    return render(request, 'app/index.html', context)


def patient_detail(request, patient_id):
    try:
        p = Patient.objects.get(pk=patient_id)
        room = Room.objects.get(patient=p)

        p_info_text = ["pacienta id", "vārds", "uzvārds", "personas kods", "adrese", "telefona numurs"]
        p_info_data = [p.patient_id, p.name, p.surname, p.p_number, p.address, p.phone]
        
        p_care_text = ["pieņemšanas datums", "izrakstīšanās datums", "stāvoklis"]
        p_care_data = [p.care_date_from, p.care_date_to, p.medical_state_name()]

        p_info = zip(p_info_text, p_info_data)
        p_care = zip(p_care_text, p_care_data)

        sick_history = p.sick_history.all()
        med_history = p.medicament_history.all()
        print(med_history.count())

    except Patient.DoesNotExist:
        raise Http404("Patient does not exist")

    queryset =  {'patient': p, 
                'patient_info': p_info, 
                'patient_care': p_care, 
                'sick_history': sick_history, 
                'room': room,
                'med_history': med_history}
    return render(request, 'patients/detail.html', queryset)


def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    room = Room.objects.get(patient=patient)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient, c_room=room)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, "Successfully updated patient")
            return redirect("patient_detail", patient.patient_id)
    else:
        form = PatientForm(instance=patient, c_room=room)
    return render(request, 'patients/edit.html', {'form': form })


def patient_new(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, "Successfully created patient")
            patient_id = data.patient_id
            return redirect("patient_detail", patient_id)
    else:
        form = PatientForm()
    return render(request, 'patients/edit.html', {'form': form})



def sick_history_detail(request, sick_hist_id):
    try:
        s = SickHistory.objects.get(pk=sick_hist_id)
        s_text = ["slimības vēstures id", "pacients",  "cēlonis", "saslimšanas datums"]
        s_data = [s.sick_hist_id, s.patient.full_name(), s.cause, s.date_sickness]
        s_info = zip(s_text, s_data)

    except SickHistory.DoesNotExist:
        raise Http404("Sick history does not exist")
    return render(request, 'sick_history/detail.html', {'sick_history_info': s_info, 'sick_history': s})


def sick_history_delete(request, sick_hist_id):
    try:
        s = SickHistory.objects.get(pk=sick_hist_id)
        patient_id = s.patient.patient_id
        s.delete()
        messages.success(request, "Successfully deleted sick history")

    except SickHistory.DoesNotExist:
        raise Http404("Sick history does not exist")
    return redirect("patient_detail", patient_id)


def sick_history_new(request, patient_id):
    patient = Patient.objects.filter(pk=patient_id)[0]

    if request.method == "POST":
        form = SickHistoryForm(request.POST, pat=patient)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, "Successfully created medical history")
            return redirect("patient_detail", patient_id)
    else:
        form = SickHistoryForm(pat=patient)
    return render(request, 'sick_history/edit.html', {'form': form, 'patient_id': patient_id})


def sick_history_edit(request, pk):
    sick_history = get_object_or_404(SickHistory, pk=pk)
    patient = sick_history.patient

    if request.method == "POST":
        form = SickHistoryForm(request.POST, pat=patient, instance=sick_history)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, "Successfully updated medical history")
            return redirect("patient_detail", patient.patient_id)
    else:
        form = SickHistoryForm(instance=sick_history, pat=patient)
    return render(request, 'sick_history/edit.html', {'form': form, 'patient_id': patient.patient_id})
    


def med_history_delete(request, pk):
    try:
        m = MedHistory.objects.get(pk=pk)
        patient_id = m.patient.patient_id
        m.delete()
        messages.success(request, "Successfully deleted medical history")

    except MedHistory.DoesNotExist:
        raise Http404("Medical history does not exist")
    return redirect("patient_detail", patient_id)


def med_history_edit(request, pk):
    med_history = get_object_or_404(MedHistory, pk=pk)
    patient = med_history.patient

    if request.method == "POST":
        form = MedHistoryForm(request.POST, pat=patient, instance=med_history)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, "Successfully updated medicament history")
            return redirect("patient_detail", patient.patient_id)
    else:
        form = MedHistoryForm(instance=med_history, pat=patient)
    return render(request, 'med_history/edit.html', {'form': form, 'patient_id': patient.patient_id})


def med_history_new(request, patient_id):
    patient = Patient.objects.filter(pk=patient_id)[0]

    if request.method == "POST":
        form = MedHistoryForm(request.POST, pat=patient)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, "Successfully created medicament history")
            return redirect("patient_detail", patient_id)
    else:
        form = MedHistoryForm(pat=patient)
    return render(request, 'med_history/edit.html', {'form': form, 'patient_id': patient_id})



def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    patient = room.patient

    if request.method == "POST":
        form = SickHistoryForm(request.POST, pat=patient)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, "Successfully updated medical history")
            return redirect("patient_detail", patient.patient_id)
    else:
        form = SickHistoryForm(instance=sick_history, pat=patient)
    return render(request, 'sick_history/edit.html', {'form': form, 'patient_id': patient.patient_id})


    