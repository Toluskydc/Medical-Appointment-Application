from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from middleware import medical_appointment_middleware

from routers.patient import patient_router
from routers.doctor import doctor_router
from routers.appointment import appointment_router
from logger import logger

app = FastAPI()
logger.info("Starting Medical Appointment App")

app.add_middleware(BaseHTTPMiddleware, dispatch=medical_appointment_middleware)



app.include_router(patient_router, prefix='/patients', tags=['Patient'])
app.include_router(doctor_router, prefix='/doctors', tags=['Doctor'])
app.include_router(appointment_router, prefix='/appointments', tags=['Appointment'])

@app.get('/')
def home():
    return {'message': 'Welcome to My Medical Appointment Application.'}