import mysql.connector
import datetime
def getConnection():
    connection = mysql.connector.connect(user="root",database = "Employee")
    return connection



