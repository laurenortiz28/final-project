import sqlite3
conn = sqlite3.connect('employeedata.db')
c=conn.cursor()

many_employees = [
                    (3765,'Olivia', 'Anderson', 5551234567, 1, 'morning', '..5@spot.com', 'barista', 25, 'Monday_Tuesday'),
                    (8921,'Ethan', 'Martinez', 5559876543, 1, 'morning', '..1@spot.com', 'barista', 21, 'Tuesday_Wednesday'),
                    (4532,'Sophia', 'Reynolds', 5554567890, 1, 'morning', '..2@spot.com', 'barista', 15, 'Monday_Wednesday'),
                    (6189,'Liam', 'Thompson', 5557891234, 1, 'morning', '..9@spot.com', 'barista', 13, 'Monday_Thursday'),
                    (1274,'Noah', 'Walker', 5552345678, 1, 'morning', '..4@spot.com', 'barista', 33, 'Tuesday_Thursday'),
                    (9408,'Jack', 'Smith', 5558765432, 1, 'noon', '..4@spot.com', 'barista', 41, 'Wednesday_Thursday'),
                    (5632,'Aidan', 'Harris', 5554321098, 1, 'noon', '..2@spot.com', 'barista', 50, 'Thursday_Friday'),
                    (7196,'Mitchell', 'Harper', 5552105432, 1, 'noon', '..6@spot.com', 'barista', 59, 'Monday_Friday'),
                    (3850,'Lucas', 'Green', 5556782345, 1, 'noon', '..0@spot.com', 'barista', 62, 'Tuesday_Friday'),
                    (2467,'Charlotte', 'Turner', 5555439876, 1, 'noon', '..7@spot.com', 'manager', 600, 'Wednesday_Friday'),
                    (8013,'Mason', 'Hall', 5556789012, 2, 'morning', '..3@spot.com', 'barista', 80, 'Thrusday_Friday'),
                    (5724,'Isabella', 'Butler', 5553217654, 2, 'morning', '..4@spot.com', 'barista', 90, 'Monday_Saturday'),
                    (1398,'Caleb', 'Nelson', 5558901234, 2, 'morning', '..8@spot.com', 'barista', 100, 'Tuesday_Saturday'),
                    (6247,'Amy', 'Price', 5555432345, 2, 'morning', '..7@spot.com', 'barista', 140, 'Wednesday_Saturday'),
                    (9754,'Henry', 'Clark', 5556754312, 2, 'morning', '..4@spot.com', 'barista', 180, 'Thrusday_Saturday'),
                    (3021,'Abigail', 'White', 5559873210, 2, 'noon', '..1@spot.com', 'barista', 200, 'Friday_Saturday'),
                    (3820,'Samuel', 'Baker', 5551238991, 2, 'noon', '..0@spot.com', 'barista', 240, 'Monday_Sunday'),
                    (2123,'Rachel', 'Mack', 5554763112, 2, 'noon', '..3@spot.com', 'barista',350, 'Tuesday_Sunday'),
                    (8561,'Peggy', 'Peterson', 5556618977, 2, 'noon', '..1@spot.com', 'barista', 400, 'Wednesday_Sunday'),
                    (1244,'John', 'Koob', 5559230034, 2, 'noon', '..4@spot.com', 'manager', 800, 'Saturday_Sunday')     
                ]
c.executemany("INSERT INTO employee VALUES (?,?,?,?,?,?,?,?,?,?)", many_employees)
conn.commit()
conn.close()