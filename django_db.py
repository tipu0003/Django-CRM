import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='mysql'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE django_db")

print("Database setup done|||")
