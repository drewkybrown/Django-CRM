# Install mysql-connector-python
# pip install mysql-connector-python
#

import mysql.connector

dataBase = mysql.connector.connect(host="localhost", user="root", password="Fucklies!")

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE  drewco")

print("Database created")
