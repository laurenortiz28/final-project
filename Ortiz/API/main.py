from fastapi import FastAPI
from employee import Employee
from get_id import getEmpinfo
from employee import LogIn
from LogIn import getLogIn
from get_shifts import getShift
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=['*'],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"]
)

@app.get("/API/employee/{emp_id}")
async def get_user_id(emp_id):
    return getEmpinfo(emp_id)


@app.post("/API/employee/log_in")
async def post_log_in(logIn: LogIn):
    return getLogIn(logIn.employee_id, logIn.password)

@app.get("/API/shift/{emp_id}")
async def getShifts(emp_id):
    return getShift(emp_id)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
