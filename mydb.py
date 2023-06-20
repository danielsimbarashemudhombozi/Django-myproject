import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '6475dany1999'
)
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE chipinge")

print("All Done")