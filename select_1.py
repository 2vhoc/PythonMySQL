import mysql.connector as mc
mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "29082005",
    database = "pythonsql"
    
)
mycs = mydb.cursor()
mycs.execute(
    "SELECT Name, NumberPhone FROM nameTable"

)
result = mycs.fetchall()
for value in result:
    print(value)
