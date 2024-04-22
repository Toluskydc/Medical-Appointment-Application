from pydantic import BaseModel
from schemas.doctor import Doctor, doctors
from schemas.patient import Patient, patients
from typing import Optional

class Appointments(BaseModel):
    id: int
    patient: Patient
    doctor: Doctor
    date: Optional[str]
    completed: Optional[bool] = False

class AppointmentCreate(BaseModel):
    patient: int
    date: Optional[str]

class AppointmentComplete(BaseModel):
    appointment_id: int
    date: Optional[str]

class AppointmentCancelled(BaseModel):
    appointment_id: int




appointments: list[Appointments] = [
    Appointments(
        id=0, patient=patients[0], doctor=doctors[1], date="2024-20-7"
    )
]

# appointments: list[Appointments] = []