from fastapi import APIRouter, status, HTTPException

from services.patient import patient_service, PatientService
from schemas.patient import Patient, patients, PatientCreate

patient_router = APIRouter()


@patient_router.get('')
def home():
    return {"message": "Welcome on board Patients"}



@patient_router.get('/', status_code=status.HTTP_200_OK)
def get_patients():
    data = patient_service.parse_patients(patient_data=patients)
    return {'message': 'successful', 'data': data}


@patient_router.get('/{patient_id}', status_code=status.HTTP_200_OK)
def get_patient_by_id(patient_id: int):
    data = PatientService.get_patient_by_id(patient_id)
    return {'message': 'Patient found successfully!', 'data' : data}


@patient_router.post('/new_patient/', status_code=status.HTTP_201_CREATED)
def create_patient(payload: PatientCreate):
    data = PatientService.create_patient(payload)
    return {'message': 'Patient created successfully', 'data': data}



@patient_router.put('/{patient_id}', status_code=status.HTTP_200_OK)
def edit_patient(patient_id: int, payload: PatientCreate):
    data = PatientService.edit_patient(patient_id, payload)
    return {'message': 'success, patient profile edited', 'data': data}

@patient_router.delete('/remove_patient/{patient_id}', status_code=status.HTTP_200_OK)
def delete_patient(patient_id: int):
    PatientService.delete_patient(patient_id)
    return {'messge': 'Patient deleted successfully.'}
 

