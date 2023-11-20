import sqlite3

conn = sqlite3.connect('employeedata.db')
c = conn.cursor()


c.execute('''
    CREATE TABLE manager_approval (
        id INTEGER PRIMARY KEY,
        employee_id INTEGER,
        manager_approval_status TEXT,
        max_pto TEXT,
        FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
    )
''')

conn.commit()
conn.close()
