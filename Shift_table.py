import sqlite3
conn = sqlite3.connect('employeedata.db')
c=conn.cursor()

c.execute("""CREATE TABLE shift(
          employee_id INTEGER fFOREIGN KEY,
          first_shift TEXT,
          second_shift TEXT,
          cafe_id INTEGER          

)""")

conn.commit()
conn.close()