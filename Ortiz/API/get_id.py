import sqlite3

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