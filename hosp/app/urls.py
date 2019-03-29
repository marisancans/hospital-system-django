from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patients/<int:patient_id>/', views.detail_patient, name='detail'),
]