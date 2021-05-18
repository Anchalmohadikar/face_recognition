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




class Face_Recognition_system:
    """ this is for screen"""
    def __init__(self,root):
        self.root=root
        self.root.configure(bg='black')
        self.root.geometry("1500x770+0+0")
        self.root.title("Attendence management system")


   
        
        

#1st image
        img=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\img1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg=ImageTk.PhotoImage(img)



        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500, height=130)

#2nd image
        img1=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\images2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg1=ImageTk.PhotoImage(img1)



        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500, height=130)
#3rd image
        img2=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\img1.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg2=ImageTk.PhotoImage(img2)



        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500, height=130)

        #title label
        title_lbl=Label(self.root, text="ATTENDENCE MANAGEMENT SYSTEM SOFTWARE", 
        font=("times new roman",35,"bold","italic"),
        bg="white",
        fg="blue"
        )

        title_lbl.place(x=0,y=130,width=1500,height=45)

        #Time
        def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text = string)
                lbl.after(1000, time)

        lbl = Label(title_lbl, font = ('Arial',14,'bold'),bg='white',fg='#25383C')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        #Attendies button
        img3=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\Atten.jpg")
        img3=img3.resize((200,200),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b1=Button(self.root, image=self.photoimg3, cursor="hand2")
        b1.place(x=200,y=200,width=200, height=150)

        b1_1=Button(self.root, text="Attendies details",command=self.details,cursor="hand2" ,font=("times new roman",15,"bold","italic"),
        bg="red",
        fg="blue"
        )
        b1_1.place(x=200,y=320,width=200, height=40)

        #detect face button

        img4=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\Attendie.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(self.root, image=self.photoimg4,cursor="hand2")
        b1.place(x=450,y=200,width=200, height=150)

        b1_1=Button(self.root, text="Face detector",cursor="hand2" ,font=("times new roman",15,"bold","italic"),
        bg="red",
        fg="blue"
        )
        b1_1.place(x=450,y=320,width=200, height=40)

         #Attendece

        img5=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\Attendence.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(self.root, image=self.photoimg5,cursor="hand2")
        b1.place(x=700,y=200,width=200, height=150)

        b1_1=Button(self.root, text="Attendence",cursor="hand2" ,font=("times new roman",15,"bold","italic"),
        bg="red",
        fg="blue"
        )
        b1_1.place(x=700,y=320,width=200, height=40)

        #help
        

        img6=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\help.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(self.root, image=self.photoimg6,cursor="hand2")
        b1.place(x=950,y=200,width=200, height=150)

        b1_1=Button(self.root, text="Help",command=self.Help,cursor="hand2",font=("times new roman",15,"bold","italic"),
        bg="red",
        fg="blue"
        )
        b1_1.place(x=950,y=320,width=200, height=40)

#exit

        img7=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\exit.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(self.root, image=self.photoimg7,cursor="hand2")
        b1.place(x=950,y=400,width=200, height=150)

        b1_1=Button(self.root, text="Exit",cursor="hand2",command=self.iexit ,font=("times new roman",15,"bold","italic"),
        bg="red",
        fg="blue"
        )
        b1_1.place(x=950,y=520,width=200, height=40)

#develper face btn
        
        img8=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\developers.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(self.root, image=self.photoimg8,cursor="hand2",command=self.Developers)
        b1.place(x=700,y=400,width=200, height=150)

        b1_1=Button(self.root, text="Developers",cursor="hand2",command=self.Developers,font=("times new roman",15,"bold","italic"),
        bg="red",
        fg="blue"
        )
        b1_1.place(x=700,y=520,width=200, height=40)

#photos
        img9=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\photos.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(self.root, image=self.photoimg9,cursor="hand2")
        b1.place(x=450,y=400,width=200, height=150)

        b1_1=Button(self.root, text="Photos",cursor="hand2" ,font=("times new roman",15,"bold","italic"),
        bg="red",
        fg="blue"
        )
        b1_1.place(x=450,y=520,width=200, height=40)


#train data
        img10=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\trin_data.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(self.root, image=self.photoimg10,cursor="hand2")
        b1.place(x=200,y=400,width=200, height=150)

        b1_1=Button(self.root, text="Train Data",cursor="hand2" ,font=("times new roman",15,"bold","italic"),
        bg="red",
        fg="blue"
        )
        b1_1.place(x=200,y=520,width=200, height=40)

       

# ********************functiom button
    def details(self):
            self.new_window= Toplevel(self.root)   
            self.app=Student(self.new_window) 

    def Developers(self):
            self.new_window= Toplevel(self.root)   
            self.app=Developers(self.new_window) 


    def Help(self):
            self.new_window= Toplevel(self.root)   
            self.app=Help(self.new_window)

    def iexit(self):
            self.iexit=tkinter.messagebox.askyesno("Face Recognition","Do you want to Exit ?",parent=self.root)
            if self.iexit >0:
                    self.root.destroy()
            else:
                    return
         
             






if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()        