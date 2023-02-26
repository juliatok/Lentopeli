import mysql.connector
import random

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

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='tietovisa',
         user='root',
         password='assiponi',
         autocommit=True
         )

arvotutmaat = arvokenttä()
for n in arvotutmaat:
    print("Arvottiin maa:",', '.join(n))
