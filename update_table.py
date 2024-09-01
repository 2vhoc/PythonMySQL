import mysql.connector as mc
mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "pythonsql"
    
)
mycs = mydb.cursor()
mycs.execute(
    "UPDATE nameTable SET Name = 'Vu Van Hoc' WHERE Name = 'V V Hoc'" 
)
mydb.commit()
