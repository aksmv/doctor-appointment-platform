from django.urls import path
from .views import (
    PatientRegisterView,
    DoctorRegisterView,
    PatientLoginView,
    DoctorLoginView
)

urlpatterns = [
    path('patient/signup', PatientRegisterView.as_view(), name='patient-register'),
    path('doctor/signup', DoctorRegisterView.as_view(), name='doctor-register'),
    path('patient/login', PatientLoginView.as_view(), name='patient-login'),
    path('doctor/login', DoctorLoginView.as_view(), name='doctor-login'),
]
