import sqlite3
from shift import Shift
import traceback

def getpstedShift(sft_id, available):

    conn = sqlite3.connect('shiftspot.db')

    try:
        sql = "UPDATE shift SET available = ? WHERE sft_id = ? "
        cursor = conn.cursor()
        cursor.execute(sql, (available, sft_id))
        conn.commit()
        return True
    except:
        traceback.print_exc()
        return False
    finally:
        conn.close()