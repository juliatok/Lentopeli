import mysql.connector
import random

käyttäjänimi = "Wimmu"

def arvokenttä(): # ARPOO KOLME MAATA TIETOKANNASTA
    kerrat = 0
    arvotutmaat = []
    while kerrat != 3:
        numero = random.randint(1,30)
        sql = "select Nimi from maat where ID = '" + str(numero) +"'"
        #print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        for n in tulos:
            if n not in arvotutmaat:
                #print(n)
                arvotutmaat.append(n)
                kerrat = kerrat + 1
    return arvotutmaat

def maanvalinta(arvotutmaat):
    kerrat = 1
    print("Hei", käyttäjänimi, "Valitse kotimaasi:")
    for n in arvotutmaat:
        if kerrat == 1:
            print("A.",', '.join(n))
            kerrat = kerrat + 1
            valinta1 = n
        elif kerrat == 2:
            print("B.",', '.join(n))
            kerrat = kerrat + 1
            valinta2 = n
        else:
            print("C.",', '.join(n))
            kerrat = kerrat + 1
            valinta3 = n
    valinta = input("-> ")
    while valinta != "A" and valinta != "B" and valinta != "C":
        print("Virheellinen syöte! Valitse A, B tai C!")
        valinta = input("-> ")
    if valinta == "A":
        print("Kotimaasi on", ', '.join(valinta1))
        valinta = valinta1
    elif valinta == "B":
        print("Kotimaasi on", ', '.join(valinta2))
        valinta = valinta2
    else:
        print("Kotimaasi on", ', '.join(valinta3))
        valinta = valinta3
    return valinta

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='tietovisa',
         user='root',
         password='assiponi',
         autocommit=True
         )

arvotutmaat = arvokenttä()
kotimaa = maanvalinta(arvotutmaat)
print(kotimaa)
