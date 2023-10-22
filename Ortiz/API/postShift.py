import sqlite3
from shift import Shift

def getpstedShift(sft_id):

    conn = sqlite3.connect('shiftspot.db')

    cursor=conn.execute('UPDATE shift SET available = "available" WHERE sft_id')
    result = cursor.fetchone()

    conn.commit()
    conn.close()


    return True