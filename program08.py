import sqlite3 as lite
con = lite.connect('mtica.db')

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute('''CREATE TABLE  Cars(
         Id INT, Name TEXT,Price INT)''')
print("table cars created.")
cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")

cur.execute("INSERT INTO Cars VALUES(3,'skoda',47678)")
cur.execute("INSERT INTO Cars VALUES(4,'volvo',36764)")
cur.execute("INSERT INTO Cars VALUES(5,'Bentley',64873)")
cur.execute("INSERT INTO Cars VALUES(6,'Citroen',84676)")
cur.execute("INSERT INTO Cars VALUES(7,'Hummer',53667)")
cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',24454)")

con.commit()
print("values in table car inserted.")
