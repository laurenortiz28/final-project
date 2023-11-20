import sqlite3

conn = sqlite3.connect('employeedata.db')
c = conn.cursor()


manager_approval = [
    (1, 3765, 'denied', '0 Days'),
    (2, 8921, 'denied', '0 Days'),
    (3, 4532, 'denied', '0 Days'),
    (4, 6189, 'denied', '0 Days'),
    (5, 1274, 'pending', 'pending medical'),
    (6, 9408, 'pending', 'pending medical'),
    (7, 5632, 'pending', 'pending medical'),
    (8, 7196, 'pending', 'pending medical'),
    (9, 3850, 'pending', 'pending medical'),
    (10, 2467, 'approved', 'up to 14 days'),
    (11, 8013, 'pending', 'pending medical'),
    (12, 5724, 'approved', 'up to 7 days'),
    (13, 1398, 'approved', 'up to 14 days'),
    (14, 6427, 'approved', 'up to 14 days'),
    (15, 9754, 'approved', 'up to 14 days'),
    (16, 3021, 'approved', 'up to 14 days'),
    (17, 2123, 'approved', 'up to 14 days'),
    (18, 8561, 'approved', 'up to 14 days'),
    (19, 1244, 'approved', 'up to 14 days')    
   
]

c.executemany("INSERT INTO ManagerApproval (id, employee_id, manager_approval_status, max_pto) VALUES (?,?,?,?)", manager_approval)

conn.commit()
conn.close()
