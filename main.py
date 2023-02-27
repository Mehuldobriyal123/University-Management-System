import collage
import courses
import delete
import display
import insert
import marksheet
import tables
import update
import defn


def adminid():
    eid=int(input("Enter Six Digit Admin Id:\t"))
    if eid==123456:
        password()
    else:
        print("Wrong ID")
        print("Please Enter Valid Admin Id")
        print("="*120)
        adminid()
        
     

def password():
    password=int(input("Enter Password:\t"))
    if password==1234:
        while True:
            print("="*120)
            print("++++++++++++++ WELCOME ADMIN TO UNIVERSITY +++++++++++++\n\n ")
            print("1)DISPLAY list of Colleges")
            print("2)SEARCH for a Colleges in University Database ")
            print("3)To do UPDATION in a University's college list Database ")
            print("4)INSERT New college in University Database")
            print("5)DELETE collage from University Database")
            print("6)DISPLAY list of Students")
            print("7)SEARCH for student in college's Database ")
            print("8)To do UPDATE in a Student Database ")
            print("9)INSERT New Student in college's Database")
            print("10)DELETE New student from college's Database")
            print("11)To Go to Main Menu")
            print("="*120)
            ch=int(input("\t\t\tEnter Your Choice\t"))
            if ch==1:
                display.display_collage()
            elif ch==2:
                defn.searchinclg()
            elif ch==3:
                defn.updinclg()
            elif ch==4:
                insert.insert_into_collage()
            elif ch==5:
                defn.delfrmclg()
            elif ch==6:
                display.display_uit_student()
            elif ch==7:
                defn.searchinuitstudent()
            elif ch==8:
                defn.updinuitstudent()
            elif ch==9:
                insert.insert_into_uit_students()
            elif ch==10:
                defn.delfrmuitstu()
            elif ch==11:
                choice()
                break
            else:
                print("Wrong Choice")
                print("Enter Valid Choice")
                choice()
                break
    else:
        print("Wrong Password\n")
        print("Please Enter Right password")
        adminid()




                
                

def choice():
    print("\n\n1. For Admin Login\n2. For Student Login\n3. For Exit")
    choice=int(input("\nSelect Option:\t"))
    if choice==1:
        adminid()
    elif choice==2:
        studentenroll()
    elif choice==3:
        print("\n\n\t\t+++++++++++++Thank You++++++++++++")
        print("\n\n\t\t===========Made By Gagan Zarbade=========")
    else:
        print("\n\n\t\t+++++++++++++Thank You++++++++++++")
        print("\n\n\t\t===========Made By Gagan Zarbade=========")

        








def password1():
    password1=int(input("Enter Your password:\t"))
    if password1==1234:
        while True:
            print("="*120)
            print("++++++++Welcome to Student++++++++++\n\n")
            print("1.Student Marksheet ")
            print("2.Go to Main Menu")
            ch=int(input("\nEnter your choice:\t"))
            if ch==1:
                marksheet.search_to_marksheet4()
            elif ch==2:
                choice()
                break
            else:
                print("Wrong Choice")
                print("Enter Valid Choice")
                choice()
                break
    else:
        print("Wrong Password\n")
        print("Please Enter Right password")
        studentenroll()
                
        
def studentenroll():
    eid=int(input("Enter Student enroll number:"))
    if eid==10001:
        password1()
    else:
        print("Wrong Enrollment Number\n")
        print("Enter Right Enrollment Number\n")
        studentenroll()
choice()




    
