import mysql.connector
import random


#LOPPUPISTEET
"""def loppupisteet(Nimi):
    sql = "select pisteet from käyttäjä where ID ='" + str(Nimi) + "'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos"""


#PISTEIDENKERÄYS/TALLENNUS

def pisteet(K1,pisteet):
    if K1 == "Sininen":
        print("Oikein! Sait 10 pistettä.")
        pisteet = pisteet + 10
    else:
        print("Väärin meni!")
    return pisteet

loop = 1
points = 0
while loop != 0:
    K1 = input("Minkä värinen taivas on?")
    points = pisteet(K1,points)
    print(f"Sait yhteensä {points} pistettä!")

#TOPPISTEET



"""yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='keltainenKoira123',
         autocommit=True
         )"""