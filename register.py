from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from student import Student
import mysql.connector
from tkinter import messagebox


class Register:
    """ this is for screen"""
    def __init__(self,root):
        self.root=root
        self.root.configure(bg='black')
        self.root.geometry("1500x770+0+0")
        self.root.title("Attendence management system")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ANCHAL\Desktop\face_recognition\face_detection_img\login 2.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white") #bd for border
        frame.place(x=580,y=170,width=480,height=450)

        register_lbl=Label(frame,bg="white",text="Register Here",font=("times new roman",30,"bold","italic"))
        register_lbl.place(x=20,y=20)


        Name_lbl=Label(frame, text="Name:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        Name_lbl.place(x=50,y=100)

        Name_entry=ttk.Entry(frame, width=31)
        Name_entry.place(x=50,y=130,width=250)

        email=Label(frame, text="Email:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        email.place(x=50,y=170)

        email_entry=ttk.Entry(frame, width=31)
        email_entry.place(x=50,y=200,width=250)

        password=lbl=Label(frame,text="password",font=("times new roman",15,"bold","italic"),
        bg="white",
        )
        password.place(x=50,y=240)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"italic"))   
        self.txtpass.place(x=50,y=270,width=270)

        password=lbl=Label(frame,text="Confirm password",font=("times new roman",15,"bold","italic"),
        bg="white",
        )
        password.place(x=50,y=310)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"italic"))   
        self.txtpass.place(x=50,y=340,width=270)

        check_btn=Checkbutton(frame,text="I Agree the terms and conditions",font=("times new roman",10,"bold"),onvalue=1,offvalue=0)
        check_btn.place(x=50,y=370)


        detect_btn=Button(frame,text="Register",font=("times new roman",15,"bold"),bg="red",fg="white")
        detect_btn.place(x=50,y=400,width=120,height=35)

        


        


        




if __name__=="__main__":


    root=Tk()
    obj=Register(root)
    root.mainloop()        
