import mysql.connector
mycon = mysql.connector.connect(host="localhost", user="root", passwd="root", database="hotels")
if mycon.is_connected() == True:
    print ("connected to mysql database")
cursor = mycon.cursor()
cursor.execute ("CREATE TABLE Employee ( Employee_Name VARCHAR(80), Employee_ID INT(5), Salary INT(6), Contact_Number INT(10), Email_Address VARCHAR(150))")
cursor.execute ("INSERT INTO Employee (Employee_Name, Employee_ID, Salary, Contact_Number, Email_Address) VALUES ('{}','{}','{}','{}','{}')".format('Zakir Khan', 36849, 112309, 9366372674, 'zakhan@yahoo.co.in'))
cursor.execute ("INSERT INTO Employee (Employee_Name, Employee_ID, Salary, Contact_Number, Email_Address) VALUES ('{}','{}','{}','{}','{}')".format('Naveen Richard', 39835, 223409, 9858943285, 'naveenr@gmail.com'))
cursor.execute ("INSERT INTO Employee (Employee_Name, Employee_ID, Salary, Contact_Number, Email_Address) VALUES ('{}','{}','{}','{}','{}')".format('Amit Shah', 64739, 170960, 9948586240, 'bhakt@gmail.com'))
cursor.execute ("INSERT INTO Employee (Employee_Name, Employee_ID, Salary, Contact_Number, Email_Address) VALUES ('{}','{}','{}','{}','{}')".format('Vidya Jai', 36739, 998760, 9363724941, 'vjais@yahoo.co.in'))
cursor.execute ("INSERT INTO Employee (Employee_Name, Employee_ID, Salary, Contact_Number, Email_Address) VALUES ('{}','{}','{}','{}','{}')".format('Veda Kapoor', 46380, 289765, 9373592057, 'kapoorv@rediffmail.com'))
mycon.commit()
cursor.execute("SELECT * FROM Employee")
data1 = cursor.fetchall()
count = cursor.rowcount
print("Total no. of rows retrieved in resultset:",count)
for row in data1:
    print(row)
cursor.execute ("CREATE TABLE Bookings (Booking_ID CHAR(6), Customer_Name VARCHAR(50), Room_No INT(3), Email_ID VARCHAR (150), Check_In_Date DATE, Check_Out_Date DATE, Total_Bill INT(8))")
cursor.execute ("INSERT INTO Bookings (Booking_ID, Customer_Name, Room_No, Email_ID, Check_In_Date, Check_Out_Date, Total_Bill) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(109476,'Rajkumar Sinha', 340, 'raj.1@gmail.com', '2019-11-22', '2019-12-05',752376))
cursor.execute ("INSERT INTO Bookings (Booking_ID, Customer_Name, Room_No, Email_ID, Check_In_Date, Check_Out_Date, Total_Bill) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(107897,'Bhusham Praveen', 610, 'bhu.praveen@gmail.com', '2019-10-02', '2019-10-31', 3567495))
cursor.execute ("INSERT INTO Bookings (Booking_ID, Customer_Name, Room_No, Email_ID, Check_In_Date, Check_Out_Date, Total_Bill) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(100845, 'Yash Dutt', 230, 'y.dutt@gmail.com', '2019-10-02', '2019-10-05', 6474936))
cursor.execute ("INSERT INTO Bookings (Booking_ID, Customer_Name, Room_No, Email_ID, Check_In_Date, Check_Out_Date, Total_Bill) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(189034, 'Bhavya Soni', 210, 'bhavyaa2gmail.com', '2019-09-15', '2019-09-25', 8135956))
cursor.execute ("INSERT INTO Bookings (Booking_ID, Customer_Name, Room_No, Email_ID, Check_In_Date, Check_Out_Date, Total_Bill) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(109786,'Abisha Sharqi', 702, 'abscissa@gmail.com', '2019-09-01', '2019-09-12', 756529))
mycon.commit()
cursor.execute("SELECT * FROM Employee")
data2 = cursor.fetchall()
count2 = cursor.rowcount
print("Total no. of rows retrieved in resultset:",count2)
for x in data2:
    print(x)
