from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
from mysql.connector import Error






class Developers:
    """ this is for screen"""
    def __init__(self,root):
        self.root=root
        self.root.configure(bg='black')
        self.root.geometry("1500x770+0+0")
        self.root.title("Attendence management system")

        title_lbl=Label(self.root, text="DEVELOPERS   SECTION", 
        font=("times new roman",40,"bold","italic"),
        bg="black",
        fg="blue"
        )

        title_lbl.place(x=0,y=50,width=1500,height=45)


        main_frame=Frame(self.root,bd=2,bg="white") #bd for border
        main_frame.place(x=0,y=130,width=770,height=640)

        rmain_frame=Frame(self.root,bd=2,bg="white") #bd for border
        rmain_frame.place(x=800,y=130,width=770,height=640)

        p1main_frame=Frame(main_frame,bd=2,bg="black") #bd for border
        p1main_frame.place(x=60,y=60,width=250,height=250)

        img2=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\akp.jpg")
        img2=img2.resize((250,260),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg2=ImageTk.PhotoImage(img2)



        f_lbl=Label(p1main_frame, image=self.photoimg2)
        f_lbl.place(x=0,y=0,width=248, height=250)



        p2main_frame=Frame(main_frame,bd=2,bg="black") #bd for border
        p2main_frame.place(x=60,y=350,width=250,height=250)

        img3=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\WhatsApp Image 2021-05-15 at 19.54.19.jpeg")
        img3=img3.resize((250,260),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg3=ImageTk.PhotoImage(img3)



        f_lbl=Label(p2main_frame, image=self.photoimg3)
        f_lbl.place(x=0,y=0,width=248, height=250)


        p3main_frame=Frame(rmain_frame,bd=2,bg="black") #bd for border
        p3main_frame.place(x=70,y=60,width=250,height=250)

        img4=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\WhatsApp Image 2021-05-16 at 15.01.32.jpeg")
        img4=img4.resize((250,260),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg4=ImageTk.PhotoImage(img4)



        f_lbl=Label(p3main_frame, image=self.photoimg4)
        f_lbl.place(x=0,y=0,width=248, height=250)


        p4main_frame=Frame(rmain_frame,bd=2,bg="black") #bd for border
        p4main_frame.place(x=70,y=350,width=250,height=250)

        img5=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\WhatsApp Image 2021-05-16 at 15.05.13.jpeg")
        img5=img5.resize((250,260),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg5=ImageTk.PhotoImage(img5)


        f_lbl=Label(p4main_frame, image=self.photoimg5)
        f_lbl.place(x=0,y=0,width=248, height=250)

        #Developer info....................#
        anchal_lbl=Label(main_frame, text="Anchal Mohadikar", 
        font=("times new roman",25,"bold","italic"),
        bg="white",
    
        fg="black"        
        )

        anchal_lbl.place(x=350,y=100)


        sakshi_lbl=Label(main_frame, text="Sakshi Borkar", 
        font=("times new roman",25,"bold","italic"),
        bg="white",
    
        fg="black"
        )

        sakshi_lbl.place(x=350,y=400)


        priyanka_lbl=Label(rmain_frame, text="Priyanka Chopade", 
        font=("times new roman",25,"bold","italic"),
        bg="white",
    
        fg="black"
        )

        priyanka_lbl.place(x=350,y=100)


        
        pranoti_lbl=Label(rmain_frame, text="Pranoti Shahakar", 
        font=("times new roman",25,"bold","italic"),
        bg="white",
    
        fg="black"
        )

        pranoti_lbl.place(x=350,y=400)








        




        



       
        















if __name__=='__main__':

         root=Tk()
         obj=Developers(root)
         root.mainloop()
                      
        
























        