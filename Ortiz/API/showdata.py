import sqlite3
conn = sqlite3.connect('shiftspot.db')
c=conn.cursor()
c.execute("SELECT * FROM employee")

items = c.fetchall()

print("\t" + "\t"+"\t""List of Employee Information")
print("\t" + "\t"+"\t""----------------------------")

for item in items:
    print(item)

conn.commit()
conn.close()