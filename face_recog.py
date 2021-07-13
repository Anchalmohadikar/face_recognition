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
import sqlite3





class Face_recog:
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



    # face_recognition

    def face_detect(self):
    
        faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        cam=cv2.VideoCapture(0)
        rec=cv2.createLBPHFaceRecognizer()
        rec.load("classifier.xml")
        font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX,0.4,1,0,1)

    def getProfile(id):


        conn=mysql.connector.connect(host="localhost",username="root",password="Anchal@1234",database="face_recognition")
        my_cursur=conn.cursor()
        
    while(True):
        ret,img=cv2.read()
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:

            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            profile=getProfile(id)
            if(profile!=None):

                cv2.cv.PutText(cv2.cv.fromarray(img),"Name : "+str(profile[1]),(x,y+h+20),font,(0,255,0))
                cv2.cv.PutText(cv2.cv.fromarray(img),"Age : "+str(profile[2]),(x,y+h+45),font,(0,255,0))
                cv2.cv.PutText(cv2.cv.fromarray(img),"Gender : "+str(profile[3]),(x,y+h+70),font,(0,255,0))
                cv2.cv.PutText(cv2.cv.fromarray(img),"Criminal Records : "+str(profile[4]),(x,y+h+95),font,(0,0,255))
                cv2.imshow("Face",img)
            if(cv2.waitKey(1)==ord('q')):
               break
    cam.release()
    cv2.destroyAllWindows()    





        



if __name__=="__main__":
    root=Tk()
    obj=Face_recog(root)
    root.mainloop()        
