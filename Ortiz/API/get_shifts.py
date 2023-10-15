import sqlite3
from shift import Shift

def getShift(emp_id):

    conn = sqlite3.connect('shiftspot.db')

    cursor=conn.execute('SELECT sft_id, cafe_id, employee_id, shift_id, day_of_week FROM shift WHERE employee_id = ? AND day_of_week = ?' ,(emp_id, "monday",))
    result_mon = cursor.fetchone()
    cursor = conn.execute('SELECT sft_id, cafe_id, employee_id, shift_id, day_of_week FROM shift WHERE employee_id = ? AND day_of_week = ?',(emp_id, "tuesday",))
    result_tues = cursor.fetchone()
    cursor = conn.execute('SELECT sft_id, cafe_id, employee_id, shift_id, day_of_week FROM shift WHERE employee_id = ? AND day_of_week = ?',(emp_id, "wednesday",))
    result_wed = cursor.fetchone()
    cursor = conn.execute('SELECT sft_id, cafe_id, employee_id, shift_id, day_of_week FROM shift WHERE employee_id = ? AND day_of_week = ?',(emp_id, "thursday",))
    result_thurs = cursor.fetchone()
    cursor = conn.execute('SELECT sft_id, cafe_id, employee_id, shift_id, day_of_week FROM shift WHERE employee_id = ? AND day_of_week = ?',(emp_id, "friday",))
    result_fri = cursor.fetchone()
    cursor = conn.execute('SELECT sft_id, cafe_id, employee_id, shift_id, day_of_week FROM shift WHERE employee_id = ? AND day_of_week = ?',(emp_id, "saturday",))
    result_sat = cursor.fetchone()
    cursor = conn.execute('SELECT sft_id, cafe_id, employee_id, shift_id, day_of_week FROM shift WHERE employee_id = ? AND day_of_week = ?',(emp_id, "sunday",))
    result_sun = cursor.fetchone()


    conn.close()

    shiftobject_mon = Shift()
    shiftobject_mon.sft_id = result_mon[0]
    shiftobject_mon.cafe_id = result_mon[1]
    shiftobject_mon.employee_id = result_mon[2]
    shiftobject_mon.shift_id = result_mon[3]
    shiftobject_mon.day_of_week = result_mon[4]

    shiftobject_tues = Shift()
    shiftobject_tues.sft_id = result_tues[0]
    shiftobject_tues.cafe_id = result_tues[1]
    shiftobject_tues.employee_id = result_tues[2]
    shiftobject_tues.shift_id = result_tues[3]
    shiftobject_tues.day_of_week = result_tues[4]

    shiftobject_wed = Shift()
    shiftobject_wed.sft_id = result_wed[0]
    shiftobject_wed.cafe_id = result_wed[1]
    shiftobject_wed.employee_id = result_wed[2]
    shiftobject_wed.shift_id = result_wed[3]
    shiftobject_wed.day_of_week = result_wed[4]

    shiftobject_thurs = Shift()
    shiftobject_thurs.sft_id = result_thurs[0]
    shiftobject_thurs.cafe_id = result_thurs[1]
    shiftobject_thurs.employee_id = result_thurs[2]
    shiftobject_thurs.shift_id = result_thurs[3]
    shiftobject_thurs.day_of_week = result_thurs[4]

    shiftobject_fri = Shift()
    shiftobject_fri.sft_id = result_fri[0]
    shiftobject_fri.cafe_id = result_fri[1]
    shiftobject_fri.employee_id = result_fri[2]
    shiftobject_fri.shift_id = result_fri[3]
    shiftobject_fri.day_of_week = result_fri[4]

    shiftobject_sat = Shift()
    shiftobject_sat.sft_id = result_sat[0]
    shiftobject_sat.cafe_id = result_sat[1]
    shiftobject_sat.employee_id = result_sat[2]
    shiftobject_sat.shift_id = result_sat[3]
    shiftobject_sat.day_of_week = result_sat[4]

    shiftobject_sun = Shift()
    shiftobject_sun.sft_id = result_sun[0]
    shiftobject_sun.cafe_id = result_sun[1]
    shiftobject_sun.employee_id = result_sun[2]
    shiftobject_sun.shift_id = result_sun[3]
    shiftobject_sun.day_of_week = result_sun[4]


    shifts = [shiftobject_mon, shiftobject_tues, shiftobject_wed, shiftobject_thurs, shiftobject_fri, shiftobject_sat, shiftobject_sun ]

    return shifts