import mysql.connector as con
con=con.connect(host="localhost", user="root",password="Anchal@1234",database="face_recognition")
if con.is_connected():

    print("successfully connected")

else:
    print("some")
