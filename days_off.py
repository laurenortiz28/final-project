import sqlite3
conn = sqlite3.connect('employeedata.db')

employee_id = int(input("Please enter the employee id:"))
cursor=conn.execute('SELECT days_off FROM employee WHERE employee_id = ?',(employee_id,))
result = cursor.fetchone()
if result!=None:
        print(result)
else:
     print(f'Employee with ID not found.')

conn.commit()
conn.close()