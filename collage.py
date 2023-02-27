import mysql.connector as m

con=m.connect(host="localhost",user="root",password="PleaseEnterYourPassword",database="university")

cur=con.cursor()







def search_into_collage1():
    s=input("\nEnter collage Name of whom you want to see record\t")
    q="select*from collage where  cname=%s"
    t=(s,)
    cur.execute(q,t)
    for i in cur:
        print("\nCode--->",i[0])
        print("Collage Name--->",i[1])
        print("City--->",i[2])
        print("Courses--->",i[3])
        print("="*60)
    con.commit()


def search_into_collage2():
    s=int(input("\nEnter collage code of whom you want to see record\t"))
    q="select*from collage where  code=%s"
    t=(s,)
    cur.execute(q,t)
    for i in cur:
        print("\nCode--->",i[0])
        print("Collage Name--->",i[1])
        print("City--->",i[2])
        print("Courses--->",i[3])
        print("="*60)
    con.commit()


def search_into_uit1():
    s=input("\nEnter course Name of whom you want to see record\t")
    q="select*from uit where  course=%s"
    t=(s,)
    cur.execute(q,t)
    for i in cur:
        print("\nSerial Number--->",i[0])
        print("Branch Name--->",i[1])
        print("Total Seats--->",i[2])
        print("="*60)
    con.commit()


def search_into_uit_student1():
    s=input("\nEnter Students's Enrollment number of whom you want to see record\t")
    q="select*from uit_student where  enroll=%s"
    t=(s,)
    cur.execute(q,t)
    for i in cur:
        print("\nEnrollment Number--->",i[0])
        print("Student Name--->",i[1])
        print("Branch--->",i[2])
        print("Gender--->",i[3])
        print("Blood Group--->",i[4])
        print("Mobile Number--->",i[5])
        print("="*60)
    con.commit()

def search_into_uit_student2():
    s=input("\nEnter Students's name of whom you want to see record\t")
    q="select*from uit_student where  name=%s"
    t=(s,)
    cur.execute(q,t)
    for i in cur:
        print("\nEnrollment Number--->",i[0])
        print("Student Name--->",i[1])
        print("Branch--->",i[2])
        print("Gender--->",i[3])
        print("Blood Group--->",i[4])
        print("Mobile Number--->",i[5])
        print("="*60)
    con.commit()


def search_into_uit_student3():
    s=input("\nEnter Students's mobile number of whom you want to see record\t")
    q="select*from uit_student where  mobile=%s"
    t=(s,)
    cur.execute(q,t)
    for i in cur:
        print("\nEnrollment Number--->",i[0])
        print("Student Name--->",i[1])
        print("Branch--->",i[2])
        print("Gender--->",i[3])
        print("Blood Group--->",i[4])
        print("Mobile Number--->",i[5])
        print("="*60)
    con.commit()











    
