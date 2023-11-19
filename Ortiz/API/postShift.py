import sqlite3
from shift import Shift
import traceback

def getpstedShift(sft_id, available, rqt_emp_id):

    conn = sqlite3.connect('shiftspot.db')

    try:
        sql = "UPDATE shift SET available = ?, rqt_emp_id = ? WHERE sft_id = ? "
        cursor = conn.cursor()
        cursor.execute(sql, (available, rqt_emp_id, sft_id))
        conn.commit()
        return True
    except:
        traceback.print_exc()
        return False
    finally:
        conn.close()