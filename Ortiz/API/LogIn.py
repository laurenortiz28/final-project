import sqlite3
from employee import Employee

def getLogIn(emp_id, pswd):

    conn = sqlite3.connect('shiftspot.db')

    cursor=conn.execute('SELECT employee_id, password FROM employee WHERE employee_id = ? AND password = ?',(emp_id,pswd))
    result = cursor.fetchone()

    conn.commit()
    conn.close()
    if result!=None:
        return True
    else :
        return False




