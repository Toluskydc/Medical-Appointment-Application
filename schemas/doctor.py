from pydantic import BaseModel

class Doctor(BaseModel):
    id : int
    name : str
    specialization : str
    phone : str
    is_available : bool


class DoctorCreate(BaseModel):
    name : str
    specialization : str
    phone : str
    is_available : bool



doctors: dict[Doctor] = {
    0: Doctor(
        id=0, name="Doc. Emmanuel", specialization="Cancer", phone="+2349075288156", is_available=True
    ),
    1: Doctor(
        id=1, name="Doc. James", specialization="Diabetes", phone="+2349075288156", is_available=True
    ),
    2: Doctor(
        id=2, name="Doc. Cynthia", specialization="Pregnancy", phone="+2349075288156", is_available=True
    )
}