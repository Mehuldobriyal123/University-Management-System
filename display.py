import mysql.connector as m

con=m.connect(host="localhost",user="root",password="PleaseEnterYourPassword",database="university")

cur=con.cursor()



def display_collage():
    q="select*from collage"
    cur.execute(q)
    print("\n\n+++++++LIST OF COLLEGES+++++++++\n\n")
    for i in cur:
        print(" CODE","COLLAGE ","CITY","COURSES")
        print(i)
        print("="*120)
    con.commit()

def display_uit():
    q="select*from uit"
    cur.execute(q)
    print("\n\n+++++++List Of Branches And Total Seats in UIT+++++++\n\n")
    for i in cur:
        print("S.N.","   Branch","  Total")
        print(i)
        print("="*120)
    con.commit()

def display_uit_student():
    q="select*from uit_student"
    cur.execute(q)
    print("\n\n+++++++List Of Student in UIT+++++++\n\n")
    for i in cur:
        print(" ENROLL","     NAME  ","      BRANCH","   GENDER","  B_G","     MOBILE")
        print(i)
        print("="*120)
    con.commit()





