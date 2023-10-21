import sqlite3
conn = sqlite3.connect('employeedata.db')
c=conn.cursor()

c.execute("""CREATE TABLE employee(
          employee_id INTEGER PRIMARY KEY,
          first_name TEXT,
          last_name TEXT,
          phone_number INTEGER,
          cafe_id INTEGER,
          shift_id TEXT,
          email TEXT,
          job_pos TEXT,
          length_work INTEGER,
	      days_off TEXT

)""")

conn.commit()
conn.close()