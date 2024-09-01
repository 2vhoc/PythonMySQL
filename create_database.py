import mysql.connector as mc
mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "pythonsql"
    
)
mycs = mydb.cursor()
mycs.execute("CREATE DATABASE pythonsql") # pythonsql is name database 
