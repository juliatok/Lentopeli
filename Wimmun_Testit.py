import mysql.connector
import random

käyttäjänimi = "Wimmu"

def etsimaanlentokenttä(maa):
    sql = "select airport.name from airport, maat where nimi = '" + str(maa) +"' and airport.iso_country = maat.iso_country and type = 'large_airport' order by rand() limit 1"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    length = len(tulos)
    #print(tulos)
    if length != 0:
        return tulos
    else:
        sql = "select airport.name from airport, maat where nimi = '" + str(maa) + "' and airport.iso_country = maat.iso_country and type = 'medium_airport' order by rand() limit 1"
        # print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        return tulos


def arvokolmemaata(): # ARPOO KOLME MAATA TIETOKANNASTA
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
                arvotutmaat.append(n)
                #print(n)
                kerrat = kerrat + 1
    return arvotutmaat
def arvolentokenttä(nykyinenmaa): # ARPOO KOLME MAATA JA LENTOKENTTÄÄ MIHIN LENTÄÄ SEURAAVAKSI
    arvotutmaat = arvokolmemaata()
    kerrat = 1
    print("Hei", käyttäjänimi,"Olet maassa", ''.join(nykyinenmaa[0]), "Minne haluat lentää seuraavaksi:")
    for n in arvotutmaat:
        if kerrat == 1:
            kenttä = etsimaanlentokenttä(''.join(n))
            print("A.", ''.join(n),"-", ''.join(kenttä[0]))
            kerrat = kerrat + 1
            valinta1 = [n,kenttä[0]]
        elif kerrat == 2:
            kenttä = etsimaanlentokenttä(''.join(n))
            print("B.", ''.join(n),"-", ''.join(kenttä[0]))
            kerrat = kerrat + 1
            valinta2 = [n,kenttä[0]]
        else:
            kenttä = etsimaanlentokenttä(''.join(n))
            print("C.", ''.join(n),"-", ''.join(kenttä[0]))
            kerrat = kerrat + 1
            valinta3 = [n,kenttä[0]]
    valinta = input("-> ").upper()
    while valinta != "A" and valinta != "B" and valinta != "C":
        print("Virheellinen syöte! Valitse A, B tai C!")
        valinta = input("-> ").upper()
    if valinta == "A":
        print("   Lennetään lentokentälle", ''.join(valinta1[1]))
        valinta = valinta1
    elif valinta == "B":
        print("   Lennetään lentokentälle", ''.join(valinta2[1]))
        valinta = valinta2
    else:
        print("   Lennetään lentokentälle", ''.join(valinta3[1]))
        valinta = valinta3
    return valinta


# ______________________ PÄÄOHJELMA ______________________
yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='assiponi',
         autocommit=True
         )

nykyinenmaa = ('Viro',), ('Fuerteventura Airport',)
while nykyinenmaa != 0:
    nykyinenmaa = arvolentokenttä(nykyinenmaa)
