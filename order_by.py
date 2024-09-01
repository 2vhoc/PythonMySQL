import mysql.connector as mc
mydb = mc.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "pythonsql"
    
)
mycs = mydb.cursor()
mycs.execute(
    "SELECT GPA FROM nameTable ORDER BY DESC" # DEST/ASC, Use to rows is digit

)
result = mycs.fetchall()
for value in result:
    print(value)
