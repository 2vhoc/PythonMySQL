import mysql.connector as mc
mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "pythonsql"
    
)
mycs = mydb.cursor()
mycs.execute(
    "CREATE TABLE nameTable(Name varchar(255), Address varchar(255), NumberPhone varchar(255))"

)
mydb.commit()
