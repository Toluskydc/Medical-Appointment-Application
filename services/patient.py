from schemas.patient import Patient, patients, PatientCreate
from fastapi import HTTPException,status


class PatientService:
    @staticmethod
    def parse_patients(patient_data):
        data = []
        for patient in patient_data:
            data.append(patients[patient])
        return data
    

    @staticmethod
    def get_patient_by_id(patient_id):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(detail='Patient not found.', status_code=404)
        return patient
    

    @staticmethod
    def create_patient(patient_data: PatientCreate):
        id = len(patients)
        patient = Patient(
            id=id,
            **patient_data.model_dump()
        )
        patients[id] = patient
        return patient


    @staticmethod
    def edit_patient(patient_id: int, payload: PatientCreate):
        if patient_id not in patients:
            raise HTTPException(status_code=404, detail="Patient not found")
        
        patient = patients[patient_id]
        patient.name = payload.name
        patient.age = payload.age
        patient.sex = payload.sex
        patient.weight = payload.weight
        patient.height = payload.height
        patient.phone = payload.phone
        
        return patient
    

    @staticmethod
    def delete_patient(patient_id: int):
        patient = patients.get(patient_id)
        if not patient:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Patient not found')
        del patients[patient_id]



patient_service = PatientService()