from fastapi import APIRouter, status, HTTPException


from schemas.doctor import doctors, Doctor, DoctorCreate
from services.doctor import DoctorService, doctor_service

doctor_router = APIRouter()



@doctor_router.get('')
def home():
    return {"message": "Welcom on board Doctor!"}


@doctor_router.get('/', status_code=status.HTTP_200_OK)
def get_doctors():
    data = doctor_service.parse_doctors(doctor_data=doctors)
    return {'message': 'successful', 'data': data}


@doctor_router.get('/{doctor_id}', status_code=status.HTTP_200_OK)
def get_doctor_by_Id(doctor_id: int):
    data = DoctorService.get_doctor_by_id(doctor_id)
    return {'message': 'Doctor found successfully!', 'data': data}

@doctor_router.post('/new_doctor/', status_code=status.HTTP_201_CREATED)
def create_doctor(payload: DoctorCreate):
    data = DoctorService.create_doctor(payload)
    return {'message': 'Doctor created successfully', 'data': data}

@doctor_router.put('/{doctor_id}', status_code=status.HTTP_200_OK)
def edit_doctor(doctor_id: int, payload: DoctorCreate):
    data = DoctorService.edit_doctor(doctor_id, payload)
    return {'message': 'success, Doctor profile edited', 'data': data}

@doctor_router.delete('/remove_doctor/{doctor_id}', status_code=status.HTTP_200_OK)
def delete_doctor(doctor_id: int):
    DoctorService.delete_doctor(doctor_id)
    return {'messge': 'Doctor deleted successfully.'}