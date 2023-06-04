import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user = 'proot',
    password = '1234',
)

cursorObject = db.cursor()

cursorObject.execute("CREATE DATABASE gab_db")

print("Database created")