import mysql.connector as m

con=m.connect(host="localhost",user="root",password="PleaseEnterYourPassword",database="university")

cur=con.cursor()


def collageTB():
    q="create table collage(code int primary key,cname varchar(20),city varchar(15),courses int)"
    cur.execute(q,)
    print("\n\nTable Created")

def uitTB():
    q="create table uit(sn int primary key,course varchar(20),seats int)"
    cur.execute(q,)
    print("\n\nTable Created")


def createTB_for_uit_students():
    q="create table uit_student(enroll int primary key,name varchar(30),branch varchar(30),gender varchar(10),mobile int,blood_g varchar(6))"
    cur.execute(q,)
    print("\n\nTable created")









