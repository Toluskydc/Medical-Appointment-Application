from pydantic import BaseModel

class Patient(BaseModel):
    id : int
    name: str
    age : int
    sex : str
    weight : float
    height : float
    phone : str

class PatientCreate(BaseModel):
    name: str
    age : int
    sex : str
    weight : float
    height : float
    phone : str




patients : dict[Patient] = {
    0: Patient(id=0, name="dami", age=23, sex="M", weight=548.34, height=21.01, phone="+2349075288156"),
    1: Patient(id=1, name="Toyin", age=26, sex="F", weight=598.34, height=22.03, phone="+2349075288146"),
    2: Patient(id=2, name="Sola", age=20, sex="M", weight=518.34, height=24.02, phone="+2349075288196")
}