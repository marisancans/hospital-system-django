from django.db import models

# Create your models here.

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    equipment = models.CharField(blank=False, max_length=100)
    date_assigned = models.DateTimeField(blank=False, auto_now=False, auto_now_add=False)

class Receipt(models.Model):
    receipt_id = models.AutoField(primary_key=True)
    total = models.FloatField(blank=False, default=0)
    date_crated = models.DateTimeField(auto_now_add=True)
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

class SickHistory(models.Model):
    sick_hist_id = models.AutoField(primary_key=True)
    cause = models.TextField(blank=False)
    date_sickness = models.DateField(blank=False, auto_now=False, auto_now_add=False)

class MedHistory(models.Model):
    medicament_id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=100)
    price = models.FloatField(blank=False, default=0)
    receipt_id = models.ForeignKey(Receipt, on_delete=models.SET_NULL, null=True)
    dose = models.FloatField(blank=False, default=0)


class Person(models.Model): # Base class
    name = models.CharField(blank=False, max_length=100)
    surname = models.CharField(blank=False, max_length=100)
    p_number = models.CharField(blank=False, max_length=100)
    address = models.CharField(blank=False, max_length=100)
    phone = models.CharField(blank=False, max_length=100)
    sick_hist = models.ManyToManyField(SickHistory)

class Patient(Person):
    MED_STATE = (
        ('1', 'Deadly'),
        ('2', 'Emergency'),
        ('3', 'Checkup')
    )
    patient_id = models.AutoField(primary_key=True)
    care_date_from = models.DateField(blank=False, auto_now=False, auto_now_add=False)
    care_date_to = models.DateField(blank=False, auto_now=False, auto_now_add=False)
    medical_state = models.CharField(blank=False, choices=MED_STATE, max_length=100)

    def full_name(self):
        return self.name + " " + self.surname

    def medical_state_name(self):
        return dict(self.MED_STATE).get(self.medical_state)