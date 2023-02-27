import mysql.connector as m

con=m.connect(host="localhost",user="root",password="PleaseEnterYourPassword")

cur=con.cursor()

print('''
        |     |  |\   |   -----  \        /  -----  ------  -----  ------  -------  \     /
        |     |  | \  |     |     \      /   |      |    |  |         |       |      \   /
        |     |  |  \ |     |      \    /    -----   ----   |         |       |       \ /
        |     |  |   \|     |       \  /     |      | \     |         |       |        /
         -----            -----      \/      -----  |  \    -----  ------     |       /  






        |\    /|     /\     |\    |     /\     ------   ------  |\    /|  ------  |\    |  --------
        | \  / |    /  \    | \   |    /  \    |        |       | \  / |  |       | \   |      |
        |  \/  |   /----\   |  \  |   /----\   |  |--|   ----   |  \/  |   ----   |  \  |      |
        |      |  /      \  |   \ |  /      \  |  |  |  |       |      |  |       |   \ |      |   
        |      | /        \ |    \| /        \ |--|  |   ----   |      |   -----  |    \|      |     





        --------  \      /   --------  -------   ---------   |\    /|
        |          \    /    |            |      |           | \  / |
        |______     \  /     |______      |      |_______    |  \/  |
               |     \/             |     |      |           |      |
               |     /              |     |      |           |      |
        --------    /        --------     |      --------    |      |
        ''')

cur.execute("show databases")
for i in cur:
    print(i)


print("="*78)
print("1)Search for a collages in University Database ")
print("2)For Update in a collage Database ")
print("3)Insert New collage in University Database")
print("4)Delete collage from University Database")
print("5)Show list of Collages")
print("6)Search for student in collage Database ")
print("7)Insert New Student in collage Database")
print("8)Delete New student from collage Database")
print("9)Show list of Students")
print("10)To Exit type 'EXIT' or 'exit'")










