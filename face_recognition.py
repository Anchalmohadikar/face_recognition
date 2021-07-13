from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from student import Student
import mysql.connector
from developers import Developers
from help import Help
from time import strftime
from datetime import datetime
import os
import numpy as np
import cv2
from train import Train
from tkinter import messagebox





class Face_recognition:
    """ this is for screen"""
    def __init__(self,root):
        self.root=root
        self.root.configure(bg='black')
        self.root.geometry("1500x770+0+0")
        self.root.title("Attendence management system")

    #title label
        title_lbl=Label(self.root, text="Face Detector",
        font=("times new roman",40,"bold","italic"),
        bg="white",
        fg="purple"
        )

        title_lbl.place(x=0,y=0,width=1500,height=45)

        img=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\img1.jpg")
        img=img.resize((500,150),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg=ImageTk.PhotoImage(img)



        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=45,width=500, height=150)


       


        img1=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\images2.jpg")
        img1=img1.resize((500,150),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg1=ImageTk.PhotoImage(img1)



        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500,y=45,width=500, height=150)

        img2=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\img1.jpg")
        img2=img2.resize((500,150),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg2=ImageTk.PhotoImage(img2)



        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000,y=45,width=500, height=150)


        img6=Image.open(r"C:\Users\ANCHAL\Desktop\face_recognition\face_detection_img\circle.jpg")
        img6=img6.resize((500,700),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg6=ImageTk.PhotoImage(img6)

        f_lbl=Label(self.root, image=self.photoimg6)
        f_lbl.place(x=500,y=300,width=500, height=300)

        detect_btn=Button(self.root,text="Detect Face",command=self.face_detect,font=("times new roman",25,"bold"),bg="black",fg="white",width=10)
        detect_btn.place(x=640,y=430)


    def mark_attendence(self,i,s,n,d):
        with open("Anchal.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list) and (s not in name_list) and (s not in name_list) and (s not in name_list)) :
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{s},{n},{d},{dtString},{d1},Present")

 



    # face_recognition

    def face_detect(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
             
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)


            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Anchal@1234",database="face_recognition")
                my_cursur=conn.cursor()

                my_cursur.execute("select Name from student where iID="+str(id))
                n=my_cursur.fetchone()
                n="+".join(n)
                
                my_cursur.execute("select iID from student where iID="+str(id))
                s=my_cursur.fetchone()
                s="+".join(s)
                
                my_cursur.execute("select department from student where iID="+str(id))
                d=my_cursur.fetchone()
                d="+".join(d)

                my_cursur.execute("select iID from student where iID="+str(id))
                i=my_cursur.fetchone()
                i="+".join(i)
                
                

                if confidence>77:
                    cv2.putText(img,f"Roll:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"iID:{s}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,s,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unable to detect ",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

      
        
        def recognize(img,clf,faceCascade):



            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

            
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
    
    

        video_cap=cv2.VideoCapture(0)


        while True:


            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)



           


            if cv2.waitKey(1)==13:
                break
               
            
        video_cap.release()
        cv2.destroyAllWindows()

        







    



 








if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()        