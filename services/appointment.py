from schemas.appointment import AppointmentCreate, appointments, Appointments, AppointmentComplete, AppointmentCancelled
from schemas.patient import patients
from schemas.doctor import doctors
from fastapi import HTTPException, status
class AppointmentService:

    @staticmethod
    def create_appointment(payload: AppointmentCreate):
        id = len(appointments)
        if payload.patient not in patients:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Patient profile not found. Create a profile.")
        
        patient = patients[payload.patient]
        doctor = AppointmentService.get_available_doctor()
        if doctor:
            appointment = Appointments(
            id=id,
            patient=patient,
            doctor=doctor,
            date=payload.date
            )
            appointments.append(appointment)
            return appointment
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No doctors available at the moment.")
    
    
    @staticmethod
    def get_available_doctor():
        for doctor in doctors.values():
            if doctor.is_available:
                doctor.is_available = False
                return doctor
        return None
    

    @staticmethod
    def complete_appointment(payload: AppointmentComplete):
        appointment = AppointmentService.get_appointment(payload.appointment_id)
        if appointment:
            if appointment.completed:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Appointment has already been completed.")
            else:
                appointment.completed = True
                appointment.doctor.is_available = True
                return {"message" : "Appointment completed successfully."}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")

    @staticmethod
    def get_appointment(appointment_id: int):
        for appointment in appointments:
            if appointment.id == appointment_id:
                return appointment
        return None
    

    @staticmethod
    def cancel_appointment(payload: AppointmentCancelled):
        appointment = AppointmentService.get_appointment(payload.appointment_id)
        if appointment:
            if appointment.completed:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Cannot cancel a completed appointment")
            appointments.remove(appointment)
            appointment.doctor.is_available = True
            return {"message": "Appointment is cancelled successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
    

    @staticmethod
    def set_availability_(doctor_id: int, is_available: bool):
        doctor = doctors.get(doctor_id)
        if doctor:
            doctor.is_available = is_available
            if is_available:
                return {"message": "Doctor is now available for the next patient"}
            else:
                return {"message": "Doctor is still not available for the next patient"}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Doctor not found")