import mysql.connector as m

con=m.connect(host="localhost",user="root",password="PleaseEnterYourPassword",database="university")

cur=con.cursor()

q="create table collage(code int primary key,cname varchar(20),city varchar(15),courses int)"

cur.execute(q)

print("table created")





































