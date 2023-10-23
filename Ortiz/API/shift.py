from fastapi import FastAPI
from pydantic import BaseModel

class Shift():

    def __init__(self):
        self.sft_id = 1
        self.cafe_id = 1
        self.employee_id = 3765
        self.shift_id = "morning"
        self.day_of_week = "monday"


class PostShift(BaseModel):
    sft_id = 1
    cafe_id = 1
    employee_id = 3765
    shift_id = "morning"
    day_of_week = "monday"
    available = "available"
