from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from student import Student
import mysql.connector
from tkinter import messagebox


class login_window:
    """ this is for screen"""
    def __init__(self,root):
        self.root=root
        self.root.configure(bg='black')
        self.root.geometry("1500x770+0+0")
        self.root.title("Attendence management system")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ANCHAL\Desktop\face_recognition\face_detection_img\login 2.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="#ffff9f") #bd for border
        frame.place(x=580,y=170,width=340,height=450)

        imgl=Image.open(r"C:\Users\ANCHAL\Desktop\face_recognition\face_detection_img\login icon.png")
        imgl=imgl.resize((100,100),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimgl=ImageTk.PhotoImage(imgl)



        lblimgl=Label(image=self.photoimgl,bg="black",borderwidth=0)
        lblimgl.place(x=670,y=170,width=150, height=130)

        get_str=Label(frame,text="Get started",font=("times new roman",25,"bold","italic"),
        fg="red",
        bg="#ffff9f")
        get_str.place(x=90,y=130)
        
 #label

        username=lbl=Label(frame,text="username",font=("times new roman",15,"bold","italic"),
        fg="black",
        bg="#ffff9f")
        username.place(x=70,y=175)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold","italic"))   
        self.txtuser.place(x=50,y=210,width=270)

        password=lbl=Label(frame,text="password",font=("times new roman",15,"bold","italic"),
        fg="black",
        bg="#ffff9f")
        password.place(x=70,y=250)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"italic"))   
        self.txtpass.place(x=50,y=280,width=270)

        detect_btn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bg="red",fg="white")
        detect_btn.place(x=100,y=320,width=120,height=35)

        reg_btn=Button(frame,text="Do you want to register?",font=("times new roman",15,"bold"),bg="#ffff9f",fg="black")
        reg_btn.place(x=60,y=400)

        detect_btn=Button(frame,text="Forgot password",font=("times new roman",15,"bold"),bg="#ffff9f",fg="black")
        detect_btn.place(x=80,y=360)

    def login(self):
        if self.txtuser.get()==" " or self.txtpass.get()==" ":
            messagebox.showerror("Error","All fields are required")

        elif self.txtuser.get()=="Anchal" and self.txtpass.get()=="anchuu":
            messagebox.showinfo("Success","Welcome to our face recognition attendence management system  ")
        else:
            messagebox.showerror("Invalid","Invalid username and password")




        














       



       


        









if __name__=="__main__":


    root=Tk()
    obj=login_window(root)
    root.mainloop()        
