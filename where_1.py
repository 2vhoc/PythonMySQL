import mysql.connector as mc
mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "pythonsql"
    
)
mycs = mydb.cursor()
mycs.execute(
    "SELECT Name, NumberPhone FROM nameTable WHERE Name = 'Na'"

)
result = mycs.fetchall()
for value in result:
    print(value)
