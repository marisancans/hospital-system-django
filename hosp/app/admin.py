from django.contrib import admin

from .models import Room, Receipt, SickHistory, MedHistory, Patient

admin.site.register(Room)
admin.site.register(Receipt)
admin.site.register(SickHistory)
admin.site.register(MedHistory)
admin.site.register(Patient)