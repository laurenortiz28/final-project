import sqlite3
from shift import Shift

def getappShifts(approve):

    conn = sqlite3.connect('shiftspot.db')

    cursor = conn.execute( 'SELECT sft_id, cafe_id, employee_id, shift_id, day_of_week, available, rqt_emp_id FROM shift WHERE available = ?',(approve,))
    result = cursor.fetchall()


    conn.commit()
    conn.close()

    list = []

    for i in range(len(result)):
        sftobject = Shift()
        sftobject.sft_id = result[i][0]
        sftobject.cafe_id = result[i][1]
        sftobject.employee_id = result[i][2]
        sftobject.shift_id = result[i][3]
        sftobject.day_of_week = result[i][4]
        sftobject.available = result[i][5]
        sftobject.rqt_emp_id = result[i][6]
        list.append(sftobject)
    return list
