import mysql.connector as mc
mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "29082005",
    database = "pythonsql"
    
)
mycs = mydb.cursor()
mycs.execute(
    "DELETE FROM nameTable WHERE Name = 'Hoc'"
)
mydb.commit()
