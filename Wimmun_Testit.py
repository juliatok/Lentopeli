import mysql.connector
import random



# ______________________ PÄÄOHJELMA ______________________
yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='tietovisa',
         user='root',
         password='assiponi',
         autocommit=True
         )
