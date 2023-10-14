from fastapi import FastAPI
from pydantic import BaseModel

class Employee:

    def __init__(self):
        self.first_name = "Lauren"
        self.last_name = "Ortiz"
        self.phone_number = 2147878421
        self.employee_id = 3765
        self.cafe_id = 1
        self.shift_id = "morning"
        self.email = "2345@spot.com"
        self.job_pos = "barista"

class LogIn(BaseModel):

    employee_id: int
    password: str

