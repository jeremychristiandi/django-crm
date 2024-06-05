# pip install mysql
# pip install mysql-connector or pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

# Prepare cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE djangocrm")
print("Database created.")