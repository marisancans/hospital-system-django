from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('patients/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:pk>/edit', views.patient_edit, name='patient_edit'),

    path('sick_histories/<int:sick_hist_id>/', views.sick_history_detail, name='sick_history_detail'),
    path('sick_histories/<int:sick_hist_id>/delete', views.sick_history_delete, name='sick_history_delete'),
    path('sick_histories/<int:patient_id>/new', views.sick_history_new, name='sick_history_new'),
    path('sick_histories/<int:pk>/edit', views.sick_history_edit, name='sick_history_edit'),

    path('rooms/<int:pk>/edit', views.room_edit, name='room_edit'),

    path('med_histories/<int:pk>/edit', views.med_history_edit, name='med_history_edit'),
    path('med_histories/<int:pk>/delete', views.med_history_delete, name='med_history_delete'),
    path('med_histories/<int:patient_id>/new', views.med_history_new, name='med_history_new'),
]