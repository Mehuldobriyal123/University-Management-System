import mysql.connector as m

con=m.connect(host="localhost",user="root",password="PleaseEnterYourPassword",database="university")

cur=con.cursor()




def update_in_collage1():
    u1=int(input("\n\nEnter code in which you want to update?\t"))
    u2=input("Enter collage name you want to update\t")
    q=("update collage set cname = %s where code=%s")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")


def update_in_collage2():
    u1=int(input("\n\nEnter code in which you want to update?\t"))
    u2=input("Enter courses you want to update\t")
    q=("update collage set courses = %s where code=%s")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")

def update_in_uit():
    u1=int(input("\n\nEnter Serial Number in which you want to update?\t"))
    u2=input("Enter seats you want to update\t")
    q=("update uit set seats = %s where sn=%s")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")
    
def update_in_uit_student1():
    u1=int(input("\n\nEnter Enrollment Number in which you want to do updation?\t"))
    u2=input("Enter branch name you want to update\t")
    q=("update uit_student set branch = %s where enroll=%s")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")

def update_in_uit_student2():
    u1=int(input("\n\nEnter Enrollment Number in which you want to do updation?\t"))
    u2=input("Enter Blood Group you want to update\t")
    q=("update uit_student set blood_g = %s where enroll=%s")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")

def update_in_uit_student3():
    u1=int(input("\n\nEnter Enrollment Number in which you want to do updation?\t"))
    u2=input("Enter Mobile Number which you want to update\t")
    q=("update uit_student set mobile= %s where enroll=%s")
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")
