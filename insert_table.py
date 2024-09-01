import mysql.connector as mc
mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "pythonsql"
    
)
mycs = mydb.cursor()
mycs.execute(
    "INSERT INTO nameTable(Name, Address, NumberPhone) VALUES('Hoang', 'Tuyen Quang', '123456678')"

)
mydb.commit()
