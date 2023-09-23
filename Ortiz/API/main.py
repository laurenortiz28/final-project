from fastapi import FastAPI
from employee import Employee

app = FastAPI()

@app.get("/API/employee/{emp_id}")
async def get_user_id(emp_id):
    dummy_user_data = Employee()
    return dummy_user_data

@app.get("/")
async def access_endpoint():
    return {"message": "Hello World"}