import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Serifat2$",
  database = 'restaurant'
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE restaurant")

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE bookings (id INT AUTO_INCREMENT PRIMARY KEY , firstname VARCHAR(255), secondname VARCHAR(255), email VARCHAR(255), reservationno VARCHAR(255))")

# sql = "INSERT INTO bookings (firstname, secondname, email, reservationno) VALUES (%s, %s, %s, %s)"
# val = [
#     ("Tomiwa", "Adeyanju", "tom@mail.com", "Table 1"), 
#     ("Precious", "Garba", "presh@mail.com", "Table 11"),
#     ("Daniel", "Akinje", "dant@mail.com", "Table 3"),
#     ("Tomiwa", "Lawal", "md@mail.com", "Table 15"),
#     ("Lawal", "Yusuf", "lawal15@mail.com", "Table 3"),
#     ("Olamide", "Opeyemi", "Horpi@mail.com", "Table 2"),
#     ("Victor", "Gabriel", "gab@mail.com", "Table 2"),
#     ("Mayowa", "Fatai", "mayo@mail.com", "Table 2"),
#     ("Daniel", "Lawal", "xyz@mail.com", "Table 1"),
#     ("Daniel", "Bright", "daniboy@mail.com", "Table 1"),
#     ("Dorime", "Akpan", "pinkyqueen@mail.com", "Table 2"),
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# sql = "SELECT * FROM bookings WHERE secondname LIKE '%akinje%' "
# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# sql = "SELECT * FROM bookings WHERE firstname = %s "
# val = ("Daniel",)
# mycursor.execute(sql, val)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# sql = "SELECT * FROM bookings WHERE reservationno = %s "
# val = ("Table 2",)
# mycursor.execute(sql, val)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# sql = "SELECT * FROM bookings ORDER BY firstname ASC "

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# sql = "UPDATE bookings SET email = %s WHERE email = %ab"

# val = ("Table 5","Table 2")

# mycursor.execute(sql, val)

# mydb.commit()

# mycursor.execute("SELECT * FROM bookings")
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

mycursor.execute("SELECT * FROM bookings LIMIT 2 OFFSET 7")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Testing some changes
