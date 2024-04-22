from schemas.doctor import Doctor, doctors, DoctorCreate
from fastapi import HTTPException, status


class DoctorService:
    @staticmethod
    def parse_doctors(doctor_data):
        data = []
        for patient in doctor_data:
            data.append(doctors[patient])
        return data
    
    @staticmethod
    def get_doctor_by_id(doctor_id):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(detail='Doctor not found.', status_code=404)
        return doctor
    
    @staticmethod
    def create_doctor(patient_data: DoctorCreate):
        id = len(doctors)
        patient = Doctor(
            id=id,
            **patient_data.model_dump()
        )
        doctors[id] = patient
        return patient
    
    @staticmethod
    def edit_doctor(doctor_id: int, payload: DoctorCreate):
        if doctor_id not in doctors:
            raise HTTPException(status_code=404, detail="Doctor not found")
        
        doctor = doctors[doctor_id]
        doctor.name = payload.name
        doctor.specialization = payload.specialization
        doctor.phone = payload.phone
        doctor.is_available = payload.is_available
        
        return doctor
    
    @staticmethod
    def delete_doctor(doctor_id: int):
        doctor = doctors.get(doctor_id)
        if not doctor:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Doctor not found')
        del doctors[doctor_id]





doctor_service = DoctorService()