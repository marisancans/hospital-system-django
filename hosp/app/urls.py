from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('patients/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('sick_histories/<int:sick_hist_id>/', views.sick_history_detail, name='sick_history_detail'),
    path('sick_histories/<int:sick_hist_id>/delete', views.sick_history_delete, name='sick_history_delete'),
    path('sick_histories/<int:patient_id>/new', views.sick_history_new, name='sick_history_new'),
    path('sick_histories/<int:pk>/edit', views.sick_history_edit, name='sick_history_edit'),
]