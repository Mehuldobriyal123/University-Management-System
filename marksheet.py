import mysql.connector as m

con=m.connect(host="localhost",user="root",password="PleaseEnterYourPassword",database="university")

cur=con.cursor()



def display_marksheet():
    q="select*from marksheet"
    cur.execute(q)
    for i in cur:
        print("|Roll N|","|   Name   |","|   Father Name   |","|  Mother Name  |","|  DOB   |","|G|"," S1"," S2 ","S3"," S4 ","S5","  T ","Per","Grade\n\n")
        print("="*120)
        print(i)
        
        print("="*120)
    con.commit()








def markT():
    q="create table marksheet(roll_number bigint primary key,name varchar(20),fname varchar(20),mname varchar(20),email_id varchar(20),dob bigint,gender char,sub1 int,sub2 int,sub3 int,sub4 int,sub5 int,total bigint,per int,grade char)"
    cur.execute(q)
    print("Table Created")
    con.commit

def insert_into_marksheet():
    n=int(input("\n\nEnter How many Records you want to insert in Database:\t"))
    for i in range(n):
        roll_number=int(input("\n\nEnter Student's Roll Numbar:\t"))
        name=input("Enter Student's Name:\t")
        fname=input("Enter Student's father's Name:\t")
        mname=input("Enter Student's mother's Name:\t")
        dob=int(input("Enter Student's Date Of Birth:\t"))
        gender=input("Enter Student's Gender:\t")
        sub1=int(input("Enter Student's Marks:\t"))
        sub2=int(input("Enter Student's Marks:\t"))
        sub3=int(input("Enter Student's Marks:\t"))
        sub4=int(input("Enter Student's Marks:\t"))
        sub5=int(input("Enter Student's Marks:\t"))
        total=int(input("Enter Student's Total Marks:\t"))
        per=int(input("Enter Student's Percentage:\t"))
        grade=input("Enter Grade of student:\t")
        q="Insert into marksheet values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        t=(roll_number,name,fname,mname,dob,gender,sub1,sub2,sub3,sub4,sub5,total,per,grade)
        cur.execute(q,t)
        print("\n\nData Insert Successfully")
        con.commit()

def search_to_marksheet1():
    s=input("\n\nEnter Students Name of which you want to see record\t")
    q="select*from marksheet where  name=%s"
    t=(s,)
    cur.execute(q,t)
    for i in cur:
        print("\n\nRoll Number:\t",i[0])
        print("Name:\t\t",i[1])
        print("Father's Name:\t",i[2])
        print("Mother's Name:\t",i[3])
        print("Date Of Birth:\t",i[4])
        print("Gender:\t\t",i[5])
        print("Subject 1:\t",i[6])
        print("Subject 2:\t",i[7])
        print("Subject 3:\t",i[8])
        print("Subject 4:\t",i[9])
        print("Subject 5:\t",i[10])
        print("Total Marks:\t",i[11])
        print("Percentage:\t",i[12],"%")
        print("Grade:\t\t",i[13])
        
        print("="*120)
    con.commit()

def search_to_marksheet2():
    s=input("\n\nEnter Students's Father's Name of which you want to see record\t")
    q="select*from marksheet where  fname=%s"
    t=(s,)
    cur.execute(q,t)
    for i in cur:
        print("\n\nRoll Number:\t",i[0])
        print("Name:\t\t",i[1])
        print("Father's Name:\t",i[2])
        print("Mother's Name:\t",i[3])
        print("Date Of Birth:\t",i[4])
        print("Gender:\t\t",i[5])
        print("Subject 1:\t",i[6])
        print("Subject 2:\t",i[7])
        print("Subject 3:\t",i[8])
        print("Subject 4:\t",i[9])
        print("Subject 5:\t",i[10])
        print("Total Marks:\t",i[11])
        print("Percentage:\t",i[12],"%")
        print("Grade:\t\t",i[13])
        
        print("="*120)
    con.commit()

def search_to_marksheet3():
    s=input("\n\nEnter Students's Mother's Name of which you want to see record\t")
    q="select*from marksheet where  mname=%s"
    t=(s,)
    cur.execute(q,t)
    for i in cur:
        print("\n\nRoll Number:\t",i[0])
        print("Name:\t\t",i[1])
        print("Father's Name:\t",i[2])
        print("Mother's Name:\t",i[3])
        print("Date Of Birth:\t",i[4])
        print("Gender:\t\t",i[5])
        print("Subject 1:\t",i[6])
        print("Subject 2:\t",i[7])
        print("Subject 3:\t",i[8])
        print("Subject 4:\t",i[9])
        print("Subject 5:\t",i[10])
        print("Total Marks:\t",i[11])
        print("Percentage:\t",i[12],"%")
        print("Grade:\t\t",i[13])
        
        print("="*120)
    con.commit()

def search_to_marksheet4():
    s=input("\n\nEnter Roll Number:\t")
    q="select*from marksheet where  roll_number=%s"
    t=(s,)
    cur.execute(q,t)
    for i in cur:
        print("\n\nRoll Number:\t",i[0])
        print("Name:\t\t",i[1])
        print("Father's Name:\t",i[2])
        print("Mother's Name:\t",i[3])
        print("Date Of Birth:\t",i[4])
        print("Gender:\t\t",i[5])
        print("Subject 1:\t",i[6])
        print("Subject 2:\t",i[7])
        print("Subject 3:\t",i[8])
        print("Subject 4:\t",i[9])
        print("Subject 5:\t",i[10])
        print("Total Marks:\t",i[11])
        print("Percentage:\t",i[12],"%")
        print("Grade:\t\t",i[13])
        
        print("="*120)
    con.commit()


def search_to_marksheet5():
    s=input("\n\nEnter Students's Date of Birth of which you want to see record\t")
    q="select*from marksheet where  dob=%s"
    t=(s,)
    cur.execute(q,t)
    for i in cur:
        print("\n\nRoll Number:\t",i[0])
        print("Name:\t\t",i[1])
        print("Father's Name:\t",i[2])
        print("Mother's Name:\t",i[3])
        print("Date Of Birth:\t",i[4])
        print("Gender:\t\t",i[5])
        print("Subject 1:\t",i[6])
        print("Subject 2:\t",i[7])
        print("Subject 3:\t",i[8])
        print("Subject 4:\t",i[9])
        print("Subject 5:\t",i[10])
        print("Total Marks:\t",i[11])
        print("Percentage:\t",i[12],"%")
        print("Grade:\t\t",i[13])
        
        print("="*120)
    con.commit()
        


def delete_from_marksheet1():
    d=int(input("\n\nEnter Student's Roll Number of which you want to delete record\t"))
    q1="select * from marksheet where roll_number=%s"
    qu="delete from marksheet where roll_number=%s"
    t=(d,)
    cur.execute(q1,t)
    for i in cur:
        print("\n\nRecord Deleted",d)
    con.commit()
    cur.execute(qu,t)
    con.commit()

def delete_from_marksheet2():
    d=input("\n\nEnter Student's Name of which you want to delete record\t")
    q1="select * from marksheet where name=%s"
    qu="delete from marksheet where name=%s"
    t=(d,)
    cur.execute(q1,t)
    for i in cur:
        print("\n\nRecord Deleted",d)
    con.commit()
    cur.execute(qu,t)
    con.commit()


def update_in_marksheetDOB():
    u1=int(input("\n\nEnter Roll Number in which you want to update?\t"))
    u2=int(input("Enter Date of birth you want to update"))
    q="update marksheet set dob=%s where roll_number=%s"
    t=(u2,u1)
    cur.execute(q,t)
    con.commit()
    print("\n\nData Update Sucessfully")





    
    

