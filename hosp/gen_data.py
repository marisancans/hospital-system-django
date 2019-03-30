import os, django
os.environ['DJANGO_SETTINGS_MODULE']='hosp.settings'
django.setup()

from datetime import datetime
from dateutil.relativedelta import relativedelta

from faker import Faker
fake = Faker('lv_LV')

from app.models import Room, Receipt, SickHistory, MedHistory, Patient

five_yrs_ago = datetime.now() - relativedelta(years=5)

def create_sick_history(count, patient):
    hist_set = []

    for x in range(count):
        cause = "".join(fake.paragraphs(nb=3))
        date_sickness = fake.date_between_dates(date_start=five_yrs_ago)

        p, created = SickHistory.objects.get_or_create(
            cause=cause,
            date_sickness=date_sickness, 
            patient=patient
        )
        

    return hist_set

for x in range(25):
    name = fake.first_name()
    surname = fake.last_name()
    p_number = str(fake.random_number(digits=6)) + "-" + str(fake.random_number(digits=5))
    address = fake.address()
    phone="2" + str(fake.random_number(digits=7))

    care_date_from = fake.date_between_dates(date_start=five_yrs_ago)
    care_date_to = fake.date_between_dates(date_start=care_date_from)
    
    medical_state = fake.random_int(min=1, max=3)
    
    n_hist = fake.random_int(min=1, max=5)

    p, created = Patient.objects.get_or_create(
        name=name,
        surname=surname,
        p_number=p_number,
        address=address,
        phone=phone,
        care_date_from=care_date_from,
        care_date_to=care_date_to,
        medical_state=medical_state,
    )


    sick_history_count = fake.random_int(min=5, max=25)
    create_sick_history(sick_history_count, p)

    print("Patient {} : {} with {} sick history".format(p.patient_id, created, sick_history_count))

