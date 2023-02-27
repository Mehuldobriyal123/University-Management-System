import display
import update
import delete
import collage

def updinclg():
    print("\n\n1. For Updation of Collage Name")
    print("2. For Updation of Total Courses in Any Collage")
    ch1=int(input("\n\nEnter Your Choice:\t"))
    if ch1==1:
        display.display_collage()
        update.update_in_collage1()
        display.display_collage()
        print("\n\nAre you Want to update more in collage database 'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            updinclg()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice:\t")
            updinclg()
    elif ch1==2:
        display.display_collage()
        update.update_in_collage2()
        display.display_collage()
        print("\n\nAre you Want to update more in collage database 'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N:\t")
        if ch2=='Y' or ch2=='y':
            updinclg()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            updinclg()
    else:
        print("\n\nEnter Valid Choice")
        updinclg()


def updinuitstudent():
    print("\n\n1. For Updation of Branch")
    print("2. For Updation of Blood Group")
    print("3. For Updation of Mobile Number")
    ch1=int(input("\n\nEnter Your Choice:\t"))
    if ch1==1:
        display.display_uit_student()
        update.update_in_uit_student1()
        print("\n\nAfter Updation\n\n")
        display.display_uit_student()
        print("\n\nAre you Want to update more in collage database 'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            updinuitstudent()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice:\t")
            updinuitstudent()
    elif ch1==2:
        display.display_uit_student()
        update.update_in_uit_student2()
        print("\n\nAfter Updation\n\n")
        display.display_uit_student()
        print("\n\nAre you Want to update more in collage database 'Y' for Yes/'N' for No")
        ch2=input("Enter Y or N:\t")
        if ch2=='Y' or ch2=='y':
            updinuitstudent()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            updinuitstudent()
    elif ch1==3:
        display.display_uit_student()
        update.update_in_uit_student3()
        print("\n\nAfter Updation\n\n")
        display.display_uit_student()
        print("\n\nAre you Want to update more in collage database 'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N:\t")
        if ch2=='Y' or ch2=='y':
            updinuitstudent()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            updinuitstudent()
    else:
        print("\n\nEnter Valid Choice")
        updinuitstudent()



def delfrmclg():
    print("\n\n1. Delete Record By the use of collage CODE")
    print("2. Delete Record By the use of collage NAME")
    ch1=int(input("\n\nEnter Your Choice:\t"))
    if ch1==1:
        display.display_collage()
        delete.delete_from_collage1()
        display.display_collage()
        print("\n\nAre you Want to update more in collage database 'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            delfrmclg()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            delfrmclg()
    elif ch1==2:
        display.display_collage()
        delete.delete_from_collage2()
        display.display_collage()
        print("\n\nAre you Want to update more in collage database 'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            delfrmclg()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            delfrmclg()
    else:
        print("\n\nEnter Valid Choice")
        delfrmclg()

def searchinclg():
    print("\n\n1. Search Record By Collage NAME")
    print("2. Search Record By Collage CODE")
    ch1=int(input("\n\nEnter Your Choice:\t"))
    if ch1==1:
        display.display_collage()
        collage.search_into_collage1()
        print("\n\nAre you Want to search more 'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            searchinclg()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            searchinclg()
    elif ch1==2:
        display.display_collage()
        collage.search_into_collage2()
        print("\n\nAre you Want to Search more'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            searchinclg()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            searchinclg()
    else:
        print("\n\nEnter Valid Choice")
        searchinclg()


def searchinuitstudent():
    print("\n\n1. Search Record By Enroll Number")
    print("2. Search Record By Student Name")
    print("3. Search record By Mobile number")
    ch1=int(input("\n\nEnter Your Choice:\t"))
    if ch1==1:
        display.display_uit_student()
        collage.search_into_uit_student1()
        print("\n\nAre you Want to search more 'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            searchinuitstudent()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            searchinuitstudent()
    elif ch1==2:
        display.display_uit_student()
        collage.search_into_uit_student2()
        print("\n\nAre you Want to Search more'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            searchinuitstudent()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            searchinuitstudent()
    elif ch1==3:
        display.display_uit_student()
        collage.search_into_uit_student3()
        print("\n\nAre you Want to Search more'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            searchinuitstudent()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            searchinuitstudent()
    else:
        print("\n\nEnter Valid Choice")
        searchinuitstudent()

def delfrmuitstu():
    print("\n\n1. Delete Record By Enrollment Number")
    print("2. Delete Record By Student's Name")
    print("3. Delete Record By Student's Mobile")
    ch1=int(input("\n\nEnter Your Choice:\t"))
    if ch1==1:
        display.display_uit_student()
        delete.delete_from_uit_student1()
        display.display_uit_student()
        print("\n\nAre you Want to delete more in Student database 'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            delfrmuitstu()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            delfrmuitstu()
    elif ch1==2:
        display.display_uit_student()
        delete.delete_from_uit_student2()
        display.display_uit_student()
        print("\n\nAre you Want to delete more in Student database 'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            delfrmuitstu()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            delfrmuitstu()
    elif ch1==3:
        display.display_uit_student()
        delete.delete_from_uit_student3()
        display.display_uit_student()
        print("\n\nAre you Want to delete more in Student database 'Y' for Yes/'N' for No")
        ch2=input("\t\tEnter Y or N")
        if ch2=='Y' or ch2=='y':
            delfrmuitstu()
        elif ch2=='N' or ch2=='n':
            pass
        else:
            print("\n\nEnter Valid choice")
            delfrmuitstu()
    else:
        print("\n\nEnter Valid Choice")
        delfrmuitstu()
