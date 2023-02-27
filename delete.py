import mysql.connector as m

con=m.connect(host="localhost",user="root",password="PleaseEnterYourPassword",database="university")

cur=con.cursor()




def delete_from_collage1():
    d=int(input("\n\nEnter collage code of whom you want to delete record\t"))
    ql="select*from collage where code=%s"
    qu="DELETE from collage where code=%s"
    t=(d,)
    cur.execute(ql,t)
    for i in cur:
        print("\n\nRecord Deleted",d)
    con.commit()
    cur.execute(qu,t)
    con.commit()

def delete_from_collage2():
    d=input("\n\nEnter collage name of whom you want to delete record\t")
    ql="select*from collage where cname=%s"
    qu="DELETE from collage where cname=%s"
    t=(d,)
    cur.execute(ql,t)
    for i in cur:
        print("\n\nRecord Deleted",d)
    con.commit()
    cur.execute(qu,t)
    con.commit()


def delete_from_uit1():
    d=int(input("\n\nEnter serial number of course whom you want to delete record\t"))
    ql="select*from uit where sn=%s"
    qu="DELETE from uit where sn=%s"
    t=(d,)
    cur.execute(ql,t)
    for i in cur:
        print("\n\nRecord Deleted",d)
    con.commit()
    cur.execute(qu,t)
    con.commit()

def delete_from_uit2():
    d=input("\n\nEnter course name whom you want to delete record\t")
    ql="select*from uit where course=%s"
    qu="DELETE from uit where course=%s"
    t=(d,)
    cur.execute(ql,t)
    for i in cur:
        print("\n\nRecord Deleted",d)
    con.commit()
    cur.execute(qu,t)
    con.commit()


def delete_from_uit_student1():
    d=int(input("\n\nEnter Enrollment number whom you want to delete record\t"))
    ql="select*from uit_student where enroll=%s"
    qu="DELETE from uit_student where enroll=%s"
    t=(d,)
    cur.execute(ql,t)
    for i in cur:
        print("\n\nRecord Deleted",d)
    con.commit()
    cur.execute(qu,t)
    con.commit()

def delete_from_uit_student2():
    d=input("\n\nEnter Student's Name whom you want to delete record\t")
    ql="select*from uit_student where name=%s"
    qu="DELETE from uit_student where name=%s"
    t=(d,)
    cur.execute(ql,t)
    for i in cur:
        print("\n\nRecord Deleted",d)
    con.commit()
    cur.execute(qu,t)
    con.commit()


def delete_from_uit_student3():
    d=int(input("\n\nEnter Student's mobile number whom you want to delete record\t"))
    ql="select*from uit_student where mobile=%s"
    qu="DELETE from uit_student where mobile=%s"
    t=(d,)
    cur.execute(ql,t)
    for i in cur:
        print("\n\nRecord Deleted",d)
    con.commit()
    cur.execute(qu,t)
    con.commit()























    
