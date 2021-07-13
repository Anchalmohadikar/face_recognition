from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector






class Student:
    """ this is for screen"""
    def __init__(self,root):
        self.root=root
        self.root.configure(bg='black')
        self.root.geometry("1500x770+0+0")
        self.root.title("Attendence management system")

#=================variable
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()
        self.var_id=StringVar()
        self.var_phone=StringVar()
        self.var_DOB=StringVar()
        self.var_dep=StringVar()


#1st image
        img=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\img1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS) # Antialas converts high level image into low lwvwl img
        self.photoimg=ImageTk.PhotoImage(img)



        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500, height=130)

#2nd image
        img1=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\Atten.jpg")
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
        title_lbl=Label(self.root, text="ATTENDIES DETAILS SECTION", 
        font=("times new roman",35,"bold","italic"),
        bg="white",
        fg="blue"
        )

        title_lbl.place(x=0,y=130,width=1500,height=45)


        main_frame=Frame(self.root,bd=2,bg="white") #bd for border
        main_frame.place(x=10,y=180,width=1500,height=640)

       
#right side
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",text="details")
        Right_frame.place(x=680,y=10,width=800,height=580)

        right_img=Image.open(r"C:\Users\ANCHAL\Desktop\dice_scrolling\face_detection_img\developers.jpg")
        right_img=right_img.resize((780,130),Image.ANTIALIAS)
        self.photoright_img=ImageTk.PhotoImage(right_img)

        f_lbl=Label(Right_frame, image=self.photoright_img)
        f_lbl.place(x=5,y=0, width=780,height=130)
#===search frame code==============
        search_frame=LabelFrame(main_frame,bd=2,bg="white",text="search system")
        search_frame.place(x=680,y=145,width=790,height=70)


        search_lbl=Label(search_frame, text="Search BY:", 
        font=("times new roman",15,"bold"),
        bg="green",fg="white"
        
        )#fg= forground color

        search_lbl.grid(row=0,column=0,padx=10,sticky=W)

#====search lable =======

        search_combo=ttk.Combobox(search_frame,font=("times new roman",15,"bold" ),state="readonly", width=10)

        search_combo["values"]=("select","id","phone_no.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=30)
        search_entry.grid(row=0,column=3,padx=10,sticky=W)

        search=Button(search_frame,text="Search", font=("times new roman",12,"bold"),bg="green",fg="white",width=12)
        search.grid(row=0,column=4,padx=10)

        ShowAll=Button(search_frame,text="Show All", font=("times new roman",12,"bold"),bg="green",fg="white",width=12)
        ShowAll.grid(row=0,column=5,padx=10)

#==========table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=200,width=780,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendies_table=ttk.Treeview(table_frame,column=("ID","Name","Dep","Email","phone","Add","DOB","Gender",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendies_table.xview)
        scroll_y.config(command=self.attendies_table.yview)

        self.attendies_table.heading("ID",text="ID")
        self.attendies_table.heading("Name",text="Name")
        self.attendies_table.heading("Dep",text="Department")
        self.attendies_table.heading("Email",text="Email")
        self.attendies_table.heading("phone",text="Phone")
        self.attendies_table.heading("Add",text="Address")
        self.attendies_table.heading("DOB",text="DOB")
        self.attendies_table.heading("Gender",text="Gender")
        self.attendies_table["show"]="headings"

        self.attendies_table.column("ID",width=100)
        self.attendies_table.column("Name",width=100)
        self.attendies_table.column("Dep",width=100)
        self.attendies_table.column("Email",width=100)
        self.attendies_table.column("phone",width=100)
        self.attendies_table.column("Add",width=100)
        self.attendies_table.column("DOB",width=100)
        self.attendies_table.column("Gender",width=100)
        

        self.attendies_table.pack(fill=BOTH,expand=1)
        
        self.attendies_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()



        




  
               







        




 









        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()
        self.var_id=StringVar()
        self.var_phone=StringVar()
        self.var_DOB=StringVar()
        self.var_dep=StringVar()











#left side
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",text="Details")
        Left_frame.place(x=10,y=10,width=650,height=580)
#name
        Name_lbl=Label(Left_frame, text="Name:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        Name_lbl.grid(row=0,column=0,padx=10,sticky=W)

        Name_entry=ttk.Entry(Left_frame,textvariable=self.var_name, width=31)
        Name_entry.grid(row=0,column=1,padx=10,sticky=W)

        
#id

        Id_lbl=Label(Left_frame, text="ID:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        Id_lbl.grid(row=0,column=2,padx=10,sticky=W)

        Id_entry=ttk.Entry(Left_frame,textvariable=self.var_id, width=30)
        Id_entry.grid(row=0,column=3,padx=10,sticky=W)

#email
        Email_lbl=Label(Left_frame, text="Email:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        Email_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(Left_frame,textvariable=self.var_email, width=31)
        Email_entry.grid(row=1,column=1,padx=10,sticky=W)

#phone no.
        Phone_no_lbl=Label(Left_frame, text="Phone_no.:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        Phone_no_lbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Phone_no_entry=ttk.Entry(Left_frame,textvariable=self.var_phone, width=30)
        Phone_no_entry.grid(row=1,column=3,padx=10,sticky=W)

#Address
        Add_lbl=Label(Left_frame, text="Address:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        Add_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Add_entry=ttk.Entry(Left_frame,textvariable=self.var_address, width=31)
        Add_entry.grid(row=2,column=1,padx=10,sticky=W)

#dob

        Dob_lbl=Label(Left_frame, text="DOB:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        Dob_lbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Dob_entry=ttk.Entry(Left_frame,textvariable=self.var_DOB, width=30)
        Dob_entry.grid(row=2,column=3,padx=10,sticky=W)

#gender
        Gender_lbl=Label(Left_frame, text="Gender:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        Gender_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Gender_entry=ttk.Entry(Left_frame,textvariable=self.var_gender,width=31)
        Gender_entry.grid(row=3,column=1,padx=10,sticky=W)

#department
        Dept_lbl=Label(Left_frame,  text="Department:", 
        font=("times new roman",15,"bold"),
        bg="white",
        
        )

        Dept_lbl.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        Dept_entry=ttk.Entry(Left_frame,textvariable=self.var_dep,width=30)
        Dept_entry.grid(row=3,column=3,padx=10,sticky=W)
#sticky is the west we use it if our cell is greater than widget then it will not give error

#radio button
        self.var_radio1=StringVar()
        btn1=ttk.Radiobutton(Left_frame,variable=self.var_radio1, text="Capture image sample",value="yes")
        btn1.grid(row=7, column=0)



        btn2=ttk.Radiobutton(Left_frame, text="No image sample",variable=self.var_radio1,value="no")
        btn2.grid(row=7, column=1)


        #buttons frame
        
        btn_frame=Frame(Left_frame,bd=0, relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=240,width=625,height=100)

        save=Button(btn_frame,text="submit",command=self.add_data, font=("times new roman",14,"bold"),bg="green",fg="white",width=17)
        save.grid(row=0,column=0,padx=10,pady=10)

        update=Button(btn_frame,text="update",command=self.update_data, font=("times new roman",14,"bold"),bg="green",fg="white",width=17)
        update.grid(row=0,column=2)

        delete=Button(btn_frame,text="delete",command=self.delete_data, font=("times new roman",14,"bold"),bg="green",fg="white",width=17)
        delete.grid(row=1,column=0)

        reset=Button(btn_frame,text="reset",command=self.reset_data, font=("times new roman",14,"bold"),bg="green",fg="white",width=17)
        reset.grid(row=0,column=3,padx=10)

        sample=Button(btn_frame,text="Capture image sample",command=self.generate_dataset, font=("times new roman",14,"bold"),bg="green",fg="white",width=17)
        sample.grid(row=1,column=2)

        update_img=Button(btn_frame,text="update image sample", font=("times new roman",14,"bold"),bg="green",fg="white",width=17)
        update_img.grid(row=1,column=3)

    def add_data(self):
            if self.var_name.get()=="Enter name" or self.var_dep.get()=="" or self.var_id.get()=="" :
                    messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                    try:
                            conn=mysql.connector.connect(host="localhost",username="root",password="Anchal@1234",database="face_recognition")
                            my_cursur=conn.cursor()
                            my_cursur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                       self.var_id.get(),
                                                                                                       self.var_name.get(),
                                                                                                       self.var_dep.get(),
                                                                                                       self.var_email.get(),
                                                                                                       self.var_phone.get(),
                                                                                                       self.var_address.get(),
                                                                                                       self.var_DOB.get(),
                                                                                                       self.var_gender.get()
                                                                                                ))
                            conn.commit()
                            self.fetch_data()
                            conn.close()
                            messagebox.showinfo("success","details has been added successfully",parent=self.root)
                    except Exception as es:

                            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


                  

                            

                            



    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Anchal@1234",database="face_recognition")
            my_cursur=conn.cursor()
            my_cursur.execute("select * from student")
            data=my_cursur.fetchall()

            if len(data)!=0:
                    self.attendies_table.delete(*self.attendies_table.get_children())
                    for i in data:
                            self.attendies_table.insert("",END, values=i)
                    conn.commit()
            conn.close()


            # get cursur
    def get_cursor(self,event=""):
                    cursor_focus=self.attendies_table.focus()
                
                    content=self.attendies_table.item(cursor_focus)
                    data=content["values"]


                    self.var_id.set(data[0]),
                    self.var_name.set(data[1]),
                    self.var_dep.set(data[2]),
                    self.var_email.set(data[3]),
                    self.var_phone.set(data[4]),
                    self.var_address.set(data[5]),
                    self.var_DOB.set(data[6]),
                    self.var_gender.set(data[7]) 

# update function

    def update_data(self):
             if self.var_name.get()=="Enter name" or self.var_dep.get()=="" or self.var_id.get()=="" :
                    messagebox.showerror("Error","All fields are required",parent=self.root)

             else:
                     try:
                             update=messagebox.askyesno("update","Do you want to update details?",parent=self.root)
                             if update>0:
                                     conn=mysql.connector.connect(host="localhost",username="root",password="Anchal@1234",database="face_recognition")
                                     my_cursur=conn.cursor()
                                     my_cursur.execute("update student set  Name=%s,department=%s,Email=%s,phone=%s,Address=%s,DOB=%s,Gender=%s where iID=%s",(

                                                                                                       
                                                                                                       self.var_name.get(),
                                                                                                       self.var_dep.get(),
                                                                                                       self.var_email.get(),
                                                                                                       self.var_phone.get(),
                                                                                                       self.var_address.get(),
                                                                                                       self.var_DOB.get(),
                                                                                                       self.var_gender.get(),
                                                                                                       self.var_id.get()
                                                                                                       


                                     ))
                             else:
                                      if  not update:
                                              return
                             messagebox.showinfo("success","successfully updated",parent=self.root)
                             conn.commit()
                             self.fetch_data()
                             conn.close()
                     except   Exception as es:
                             messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        

    # delete function
    def delete_data(self):
        if self.var_id.get()=="":
                messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
                try:
                        delete=messagebox.askyesno("student Delete Page","Do you want to delete details?",parent=self.root) 
                        if delete>0: 
                                 conn=mysql.connector.connect(host="localhost",username="root",password="Anchal@1234",database="face_recognition")
                                 my_cursur=conn.cursor()
                                 sql="delete from student where iId=%s"
                                 val=(self.var_id.get(),)
                                 my_cursur.execute(sql,val)
                        else:
                                if not delete:
                                        return
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("success","Sucessfully deleted",parent=self.root)

                except   Exception as es:

                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        

    def reset_data(self):
             self.var_id.set("enter roll no."),
             self.var_name.set("Enter your name"),
             self.var_dep.set("enter the dep name"),
             self.var_email.set(""),
             self.var_phone.set(""),
             self.var_address.set(""),
             self.var_DOB.set(""),
             self.var_gender.set("")

     #take photo samples
    def generate_dataset(self):
             if self.var_name.get()=="Enter name" or self.var_dep.get()=="" or self.var_id.get()=="" :
                    messagebox.showerror("Error","All fields are required",parent=self.root)

             else:
                     try:
                             
                             conn=mysql.connector.connect(host="localhost",username="root",password="Anchal@1234",database="face_recognition")
                             my_cursur=conn.cursor()
                             my_cursur.execute("select * from student")
                             myresult=my_cursur.fetchall()
                             id=0
                             for x in myresult:
                                     id+=1
                             my_cursur.execute("update student set  Name=%s,department=%s,Email=%s,phone=%s,Address=%s,DOB=%s,Gender=%s where iID=%s",(

                                                                                                       
                                                                                                       self.var_name.get(),
                                                                                                       self.var_dep.get(),
                                                                                                       self.var_email.get(),
                                                                                                       self.var_phone.get(),
                                                                                                       self.var_address.get(),
                                                                                                       self.var_DOB.get(),
                                                                                                       self.var_gender.get(),
                                                                                                       self.var_id.get()==id+1
                             ))

                             conn.commit()
                             self.fetch_data()
                             self.reset_data()
                             conn.close()

                             #=============load predefined data on frontal from open cv

                             face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                             def face_cropped(img):
                                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                     faces=face_classifier.detectMultiScale(gray,1.3,5)
                                     # scaling factor =1.3
                                     #minimum neighor =5
                                     for (x,y,w,h) in faces:
                                             face_cropped=img[y:y+h, x:x+w]
                                             return face_cropped

                             cap=cv2.VideoCapture(0)
                             img_id=0
                             while True:
                                     ret,my_frame=cap.read()
                                     if face_cropped(my_frame) is not None:
                                             img_id+=1
                                             face=cv2.resize(face_cropped(my_frame),(450,450))
                                             face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                             file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                             cv2.imwrite(file_name_path,face)
                                             cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                                             cv2.imshow("Detected face",face)

                                     if cv2.waitKey(1)==13 or int(img_id)==100:
                                             break
                             cap.release()
                             cv2.destroyAllWindows()
                             messagebox.showinfo("Result","Generating data set is completed!!!!!")
                     except   Exception as es:
                             messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                                     


                              

                                     




 
     
     
                    
        


    




                    
                      

                







       

        


       



if __name__=='__main__':

         root=Tk()
         obj=Student(root)
         root.mainloop()
                      
        


         
        
        
