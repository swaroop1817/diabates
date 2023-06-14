import sqlite3

conn=sqlite3.connect('patient.db')

cur = conn.cursor()
#cur.execute("create table patientinfo(name varchar(30),result varchar(20))")#
#cur.execute("insert into patientinfo values('xyz','diabatic')" )#
cur.execute()
conn.commit()