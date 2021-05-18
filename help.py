from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector






class Help:
    """ this is for screen"""
    def __init__(self,root):
        self.root=root
        self.root.configure(bg='black')
        self.root.geometry("1500x770+0+0")
        self.root.title("Attendence management system")


        #1st image
        img=Image.open(r"C:\Users\ANCHAL\Desktop\face_recognition\face_detection_img\img1.jpg")
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
        title_lbl=Label(self.root, text="HELP SECTION", 
        font=("times new roman",35,"bold","italic"),
        bg="white",
        fg="blue"
        )

        title_lbl.place(x=0,y=130,width=1500,height=45)



        img4=Image.open(r"C:\Users\ANCHAL\Desktop\face_recognition\face_detection_img\help2.jpg")
        img4=img4.resize((800,400),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg4=ImageTk.PhotoImage(img4)



        f_lbl=Label(self.root, image=self.photoimg4)
        f_lbl.place(x=850,y=200,width=650, height=500)


        dev_lbl=Label(self.root, text="anchalmohadikar08@gmail.com", 
        font=("times new roman",25,"bold","italic"),
        bg="black",
        fg="orange"
        )

        dev_lbl.place(x=100,y=270)



        dev1_lbl=Label(self.root, text="priyankachopade00@gmail.com", 
        font=("times new roman",25,"bold","italic"),
        bg="black",
        fg="orange"
        )

        dev1_lbl.place(x=100,y=320)


        
        dev2_lbl=Label(self.root, text="sakshiborkar343@gmail.com", 
        font=("times new roman",25,"bold","italic"),
        bg="black",
        fg="orange"
        )

        dev2_lbl.place(x=100,y=370)


        
        dev3_lbl=Label(self.root, text="pranotishahakar12@gmail.com", 
        font=("times new roman",25,"bold","italic"),
        bg="black",
        fg="orange"
        )

        dev3_lbl.place(x=100,y=420)

        dev4_lbl=Label(self.root, text="mob_no : 9850327023", 
        font=("times new roman",25,"bold","italic"),
        bg="black",
        fg="grey"
        )

        dev4_lbl.place(x=100,y=480)

        dev5_lbl=Label(self.root, text="mob_no : 8055051592", 
        font=("times new roman",25,"bold","italic"),
        bg="black",
        fg="grey"
        )

        dev5_lbl.place(x=100,y=530)


        dev5_lbl=Label(self.root, text="FEEL FREE TO CONTACT US !!", 
        font=("times new roman",35,"italic"),
        bg="black",
        fg="white"
        )

        dev5_lbl.place(x=100,y=650)





        


       






        















if __name__=='__main__':
         root=Tk()
         obj=Help(root)
         root.mainloop()
       
            

        












       











