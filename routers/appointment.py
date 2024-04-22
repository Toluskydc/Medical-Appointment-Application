from fastapi import APIRouter
from schemas.patient import patients
from schemas.appointment import Appointments, AppointmentCreate, AppointmentComplete, AppointmentCancelled
from schemas.doctor import doctors
from services.appointment import AppointmentService


appointment_router = APIRouter()

# create appointment
# complete an appointment
# cancel an appointment


@appointment_router.get('')
def home():
    return {"message": "Cheers, time for you to book an appointment with a doctor..."}

@appointment_router.post('/create')
def create_appointment(paylaod: AppointmentCreate):
    data = AppointmentService.create_appointment(paylaod)
    return data


@appointment_router.put('/complete')
def complete_appointment(paylaod: AppointmentComplete):
    data = AppointmentService.complete_appointment(paylaod)
    return data


@appointment_router.put('/cancel')
def cancel_appointment(paylaod: AppointmentCancelled):
    data = AppointmentService.cancel_appointment(paylaod)
    return data


@appointment_router.put('/set_availability')
def set_availability(doctor_id: int, is_available: bool):
    data = AppointmentService.set_availability_(doctor_id, is_available)
    return data
