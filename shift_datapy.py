import sqlite3
conn = sqlite3.connect('employeedata.db')
c=conn.cursor()

employee_shift = [
                    (3765,'morning', 1),
                    (8921,'morning', 1),
                    (4532,'morning', 1),
                    (6189,'morning', 1),
                    (1274,'morning', 1),
                    (9408,'noon', 1),
                    (5632,'noon', 1),
                    (7196,'noon', 1),
                    (3850,'noon', 1),
                    (2467,'noon', 1),
                    (8013,'morning', 2),
                    (5724,'morning', 2),
                    (1398,'morning', 2),
                    (6247,'morning', 2),
                    (9754,'morning', 2),
                    (3021,'noon', 2),
                    (3820,'noon', 2),
                    (2123,'noon', 2),
                    (8561,'noon', 2),
                    (1244,'noon', 2)     
                ]
c.executemany("INSERT INTO employee VALUES (?,?,?,?,?,?,?,?,?,?)", employee_shift)
conn.commit()
conn.close()