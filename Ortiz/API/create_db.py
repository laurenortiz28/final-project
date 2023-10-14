import sqlite3
conn = sqlite3.connect('shiftspot.db')
c=conn.cursor()


c.execute("DROP TABLE employee;")

c.execute("""
            CREATE TABLE employee(
          employee_id INTEGER PRIMARY KEY,
          first_name TEXT,
          last_name TEXT,
          phone_number INTEGER,
          cafe_id INTEGER,
          shift_id TEXT,
          email TEXT,
          job_pos TEXT,
          password TEXT
)""")
many_employees = [
                    (3765,'Olivia', 'Anderson', 5551234567, 1, 'morning', '3765@spot.com', 'barista', 'pswd123'),
                    (8921,'Ethan', 'Martinez', 5559876543, 1, 'morning', '..1@spot.com', 'barista', 'pswd123'),
                    (4532,'Sophia', 'Reynolds', 5554567890, 1, 'morning', '..2@spot.com', 'barista', 'pswd123'),
                    (6189,'Liam', 'Thompson', 5557891234, 1, 'morning', '..9@spot.com', 'barista', 'pswd123'),
                    (1274,'Noah', 'Walker', 5552345678, 1, 'morning', '..4@spot.com', 'barista', 'pswd123'),
                    (9408,'Jack', 'Smith', 5558765432, 1, 'noon', '..4@spot.com', 'barista', 'pswd123'),
                    (5632,'Aidan', 'Harris', 5554321098, 1, 'noon', '..2@spot.com', 'barista', 'pswd123'),
                    (7196,'Mitchell', 'Harper', 5552105432, 1, 'noon', '..6@spot.com', 'barista', 'pswd123'),
                    (3850,'Lucas', 'Green', 5556782345, 1, 'noon', '..0@spot.com', 'barista', 'pswd123'),
                    (2467,'Charlotte', 'Turner', 5555439876, 1, 'noon', '..7@spot.com', 'manager', 'pswd123'),
                    (8013,'Mason', 'Hall', 5556789012, 2, 'morning', '..3@spot.com', 'barista', 'pswd123'),
                    (5724,'Isabella', 'Butler', 5553217654, 2, 'morning', '..4@spot.com', 'barista', 'pswd123'),
                    (1398,'Caleb', 'Nelson', 5558901234, 2, 'morning', '..8@spot.com', 'barista', 'pswd123'),
                    (6247,'Amy', 'Price', 5555432345, 2, 'morning', '..7@spot.com', 'barista', 'pswd123'),
                    (9754,'Henry', 'Clark', 5556754312, 2, 'morning', '..4@spot.com', 'barista', 'pswd123'),
                    (3021,'Abigail', 'White', 5559873210, 2, 'noon', '..1@spot.com', 'barista', 'pswd123'),
                    (3820,'Samuel', 'Baker', 5551238991, 2, 'noon', '..0@spot.com', 'barista', 'pswd123'),
                    (2123,'Rachel', 'Mack', 5554763112, 2, 'noon', '..3@spot.com', 'barista', 'pswd123'),
                    (8561,'Peggy', 'Peterson', 5556618977, 2, 'noon', '..1@spot.com', 'barista', 'pswd123'),
                    (1244,'John', 'Koob', 5559230034, 2, 'noon', '..4@spot.com', 'manager', 'pswd123')
                ]
c.executemany("INSERT INTO employee VALUES (?,?,?,?,?,?,?,?,?)", many_employees)
conn.commit()
conn.close()
