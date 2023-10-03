import sqlite3
from employee import Employee

def GetEmpinfo(emp_id):

    conn = sqlite3.connect('shiftspot.db')

    cursor=conn.execute('SELECT first_name, last_name, phone_number, employee_id, cafe_id, shift_id, email, job_pos FROM employee WHERE employee_id = ?',(emp_id,))
    result = cursor.fetchone()



    if result!=None:
            print(result)
    else:
         print(f'Employee with ID not found.')

    conn.commit()
    conn.close()

    empobject = Employee()
    empobject.first_name = result[0]
    empobject.last_name = result[1]
    empobject.phone_number = result[2]
    empobject.employee_id = result[3]
    empobject.cafe_id = result[4]
    empobject.shift_id = result[5]
    empobject.email = result[6]
    empobject.job_pos = result[7]
    return empobject