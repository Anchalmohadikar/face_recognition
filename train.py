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
from tkinter import messagebox





class Train:
    """ this is for screen"""
    def __init__(self,root):
        self.root=root
        self.root.configure(bg='black')
        self.root.geometry("1500x770+0+0")
        self.root.title("Attendence management system")


 #title label
        title_lbl=Label(self.root, text="Train Data Set",
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


        train_btn=Button(self.root,text="TRAIN DATA",command=self.train_classifier,font=("times new roman",25,"bold"),bg="black",fg="white",width=10)
        train_btn.place(x=640,y=430)
        

    def train_classifier(self):
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
            
            faces=[]
            ids=[]

            for image in path :
        
                img=Image.open(image).convert('L')#grey scale image 
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])
            

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training",imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)
     #train classifier and save images   
        
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training data set is completed!!!!!")
            





if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()        

