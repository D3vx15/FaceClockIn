import cv2
import dlib
import cmake
import face_recognition
import face_recognition_models
import mysql.connector as sqltor
import os
import pickle

con=sqltor.connect(host="Localhost",user="root",passwd="root",database="school", auth_plugin='mysql_native_password')

if con.is_connected():
    print("Connection successful!^-^")

cursor=with.cursor()

def capture():    
 v=cv2. VideoCapture(0)
    while True:
        r,f=v.read()
        cv2.imshow("PRESS ENTER TO CAPTURE IMAGE:",f)
        k=cv2.waitKey(1)
        if k == 32:
            img_name = "current.jpg"
            cv2.imwrite(img_name, f)
            print(img_name, "written!")
            break
    v.release()
    cv2.destroyAllWindows()

def delete():
    os.remove("current.jpg")

def addstudent():
 Global cursor
    st_firstname = input("Enter the first name of the student: ")
    st_lastname = input("Enter the last name of the student: ")
    admno = int(input("Admission no. of the student: "))
    st_class= int(input("Enter the class of the student: "))
    st_section=input("Enter the section of the student: ")
    capture()
    img1=cv2.imread("current.jpg")
    a=face_recognition.face_encodings(img1)[0]
    m=str(admno)+".dat"
    f=open(m,"wb")
    pickle.dump(a,f)
    cmd="insert into stud values({},'{}','{}',{},'{}','{}','')".format(admno,st_firstname, st_lastname,st_class,st_section,m)
    cursor.execute(cmd)
    con.commit()
    delete()

def student_delete():
 Global cursor
     admno = int(input("Enter the admission number of the student to delete: "))
     sql = "delete from stud where admno = " + str(admno)
     cursor.execute(sql)
     m = str(admno) + ".dat" #place where face encodings are stored.
     try:
         os.remove(m)
         print("Face encoding file deleted successfully.")
         
     except FileNotFoundError:
         print("Face encoding file not found.")

       
def attendance():
    capture()
    #dbms parttogetencodings(make sure to add “[0]” when getting encodings
    sel=input("Enter the admission number: ")
    file=open(sel+".dat","rb")
    d=pickle.load(file)
    img=cv2.imread("current.jpg")
    b=face_recognition.face_encodings(img)[0]
    att=face_recognition.compare_faces([d],b,tolerance=0.6)
    
    if att:
        present_sql = "UPDATE stud SET attendance = 'Present' WHERE admno = {}".format(sel)
        cursor.execute(present_sql)
        con.commit()
        print("Attendance marked as Present!")  
    else:
        absent_sql = "UPDATE stud SET attendance = 'Absent' WHERE admno = {}".format(sel)
        cursor.execute(absent_sql)
        con.commit()
        print("Attendance marked as Absent.")
       
while True:
   c1=int(input('''1.add a record
2.delete a record
3.attendance
enter your choice: '''))
   if c1 == 1:
       addstudent()
       
   elif c1 == 2:
       student_delete()

   elif c1 == 3:
       attendance()
   
   else:
       print("Not an Option.")
       
   if input("press enter to continue, press any other key to exit:"):
        break
   else:
        continue