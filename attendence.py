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
import csv
from tkinter import filedialog

mydata=[]





class Attendece:
    """ this is for screen"""
    def __init__(self,root):
        self.root=root
        self.root.configure(bg='black')
        self.root.geometry("1500x770+0+0")
        self.root.title("Attendence management system")


        #variables

        self.var_atten_id=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()

    #title label
        title_lbl=Label(self.root, text="Attendence Details",
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

        main_frame=Frame(self.root,bd=2,bg="white") #bd for border
        main_frame.place(x=10,y=200,width=1500,height=640)

        #left side
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",text="Details")
        Left_frame.place(x=10,y=10,width=650,height=580)
#right prame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",text="details")
        Right_frame.place(x=680,y=10,width=800,height=580)

        table_frame=LabelFrame(Right_frame,bd=2,bg="white")
        table_frame.place(x=5,y=5,width=790,height=465)

        #scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.attendies_report_table=ttk.Treeview(table_frame,column=("Roll_ID","ID","Name","Dep","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendies_report_table.xview)
        scroll_y.config(command=self.attendies_report_table.yview)

        self.attendies_report_table.heading("Roll_ID",text="Roll_ID")
        self.attendies_report_table.heading("ID",text="ID")
        self.attendies_report_table.heading("Name",text="Name")
        self.attendies_report_table.heading("Dep",text="Department")
        self.attendies_report_table.heading("time",text="Time")
        self.attendies_report_table.heading("date",text="Date")
        self.attendies_report_table.heading("status",text="status")

        self.attendies_report_table["show"]="headings "
        self.attendies_report_table.column("Roll_ID",width=100)
        self.attendies_report_table.column("ID",width=100)
        self.attendies_report_table.column("Name",width=100)
        self.attendies_report_table.column("Dep",width=100)
        self.attendies_report_table.column("time",width=100)
        self.attendies_report_table.column("date",width=100)
        self.attendies_report_table.column("status",width=100)

        self.attendies_report_table.pack(fill=BOTH,expand=1)

        self.attendies_report_table.bind("<ButtonRelease>",self.get_cursor)










        left_inside_frame=Frame(Left_frame,bd=4,relief=RIDGE,bg="white") #bd for border
        left_inside_frame.place(x=10,y=50,width=625,height=380)
#lables ANa entry
# attendence id
        attendence_Id_lbl=Label(left_inside_frame, text=" Attendence ID:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        attendence_Id_lbl.grid(row=0,column=1,padx=10,sticky=W)

        attendence_Id_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id)
        attendence_Id_entry.grid(row=0,column=3,padx=10,sticky=W)

        #ID

        Roll_Id_lbl=Label(left_inside_frame, text="  ID:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        Roll_Id_lbl.grid(row=0,column=5,padx=10,sticky=W)

        Roll_Id_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_id)
        Roll_Id_entry.grid(row=0,column=6,padx=10,sticky=W)

#Name
        name_lbl=Label(left_inside_frame, text="  Name:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        name_lbl.grid(row=1,column=1,padx=10,sticky=W)

        name_Id_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_name)
        name_Id_entry.grid(row=1,column=3,padx=10,sticky=W)
#dep
        dep_lbl=Label(left_inside_frame, text="  Department:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        dep_lbl.grid(row=1,column=5,padx=10,sticky=W)

        dep_Id_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_dep)
        dep_Id_entry.grid(row=1,column=6,padx=10,sticky=W)
#time

        time_lbl=Label(left_inside_frame, text="  Time:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        time_lbl.grid(row=2,column=1,padx=10,sticky=W)


        time_Id_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_time)
        time_Id_entry.grid(row=2,column=3,padx=10,sticky=W)

#date
        date_lbl=Label(left_inside_frame, text=" Date:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        date_lbl.grid(row=2,column=5,padx=10,sticky=W)


        date_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_date)
        date_entry.grid(row=2,column=6,padx=10,sticky=W)
#status
        time_lbl=Label(left_inside_frame, text=" attendence status:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        time_lbl.grid(row=3,column=1,padx=10,sticky=W)


        time_Id_entry=ttk.Entry(left_inside_frame, width=20,textvariable=self.var_status)
        time_Id_entry.grid(row=3,column=3,padx=10,sticky=W)




        ##button

        btn_frame=Frame(left_inside_frame,bd=0, relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=240,width=625,height=100)

        save=Button(btn_frame,text="Import csv",command=self.importcsv, font=("times new roman",14,"bold"),bg="green",fg="white",width=10)
        save.grid(row=0,column=0,padx=10,pady=10)

        update=Button(btn_frame,text="Export csv", command=self.exportcsv,font=("times new roman",14,"bold"),bg="green",fg="white",width=10)
        update.grid(row=0,column=2)

        delete=Button(btn_frame,text="Update", font=("times new roman",14,"bold"),bg="green",fg="white",width=10)
        delete.grid(row=0,column=4)

        reset=Button(btn_frame,text="reset",command=self.reset_data, font=("times new roman",14,"bold"),bg="green",fg="white",width=10)
        reset.grid(row=0,column=3,padx=10)

    def fetchData(self,rows):


            self.attendies_report_table.delete(*self.attendies_report_table.get_children())

            for i in rows:



                    self.attendies_report_table.insert("",END, values=i)
                    #import csv===========
    def importcsv(self):
             global mydata
             mydata.clear()
             fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","* *")),parent=self.root)
             with open(fln) as myfile:
                     csvread= csv.reader(myfile,delimiter=",")
                     for i in csvread:
                             mydata.append(i)
                     self.fetchData(mydata)


    def exportcsv(self):
           try:
                     if len(mydata)<1:
                            messagebox.showerror("No Data","no data found to export",parent=self.root)
                            return False

                     fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","* *")),parent=self.root)
                     with open(fln,mode="w", newline="") as myfile:
                             exp_write=csv.writer(myfile,delimiter=",")
                             for i in mydata:
                                     exp_write.writerow(i)
                             messagebox.showinfo("Data Export","data is succesfully exported!!")

           except   Exception as es:
                             messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):


            cursor_row=self.attendies_report_table.focus()
                
            content=self.attendies_report_table.item(cursor_row)
            rows=content["values"]
            self.var_atten_id.set(rows[0]),
            self.var_id.set(rows[1]),
            self.var_name.set(rows[2]),
            self.var_dep.set(rows[3]),
            self.var_time.set(rows[4]),
            self.var_date.set(rows[5]),
            self.var_status.set(rows[6])
    
    def reset_data(self):
            self.var_atten_id.set(""),
            self.var_id.set(""),
            self.var_name.set(""),
            self.var_dep.set(""),
            self.var_time.set(""),
            self.var_date.set(""),
            self.var_status.set("")





        




                            


       













if __name__=="__main__":
    root=Tk()
    obj=Attendece(root)
    root.mainloop()        