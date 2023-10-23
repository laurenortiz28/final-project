import sqlite3
conn = sqlite3.connect('employeedata.db')

employee_id = int(input("Enter Employee ID:"))
cursor=conn.execute('SELECT length_work FROM employee WHERE employee_id = ?',(employee_id,))
result = cursor.fetchone()
if result!=None:
        _days = result[0]
        if _days < 30:
            print ("The PTO reques has been denied")
        elif _days > 30 and _days < 90:
            print  ("The PTO request has been approved only for medical matters")
        elif _days > 90 and _days < 180:
            print ("The PTO request has been approved up to 7 days")
        else:
            print ( "The PTO request has been approved up to 14 days")
  
else:
     print(f'Employee with ID not found.')

conn.commit()
conn.close()