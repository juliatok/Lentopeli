import mysql.connector
import geopy.distance
import random

syöte = 1
pisteet = 300
kuljettu_matka = 0

# ______________________ ALOITUSRUUTU ______________________
def mainmenu():
    print("Paina enter aloittaaksesi pelin.")
    print("Paina 0 lopettaaksesi ohjelman")
    syöte = input("-> ")
    while syöte != "" and syöte != 0:
        print("Virheellinen syöte!")
        print("Paina enter aloittaaksesi pelin.")
        print("Paina 0 lopettaaksesi ohjelman")
        syöte = input("-> ")
    return syöte

# __________________ KÄYTTÄJÄNIMEN KYSYNTÄ __________________
def käyttäjänimenvalinta():
    print("Anna käyttäjänimesi:")
    käyttäjänimi = input("-> ")
    return käyttäjänimi

# ______________________ ARPOO 3 MAATA ______________________
def arvokolmemaata():
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

# ______________________ KOTIMAAN VALINTA ______________________
def kotimaanvalinta():
    arvotutmaat = arvokolmemaata()
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

# ______________________ LOPPURUUTU ______________________
def end():
    print("Onneksi olkoon", käyttäjänimi, "läpäisit pelin!")
    print("Olet taas kotimaassasi", ', '.join(kotimaa))
    print("Sait", pisteet, "pistettä!")
    print("Paina 1 palataksesi päävalikkoon")
    print("Paina 0 lopettaaksesi ohjelman")
    valinta = input("-> ")
    while valinta != "1" and valinta != "0":
        print("Virheellinen syöte!")
        print("Paina 1 palataksesi päävalikkoon")
        print("Paina 0 lopettaaksesi ohjelman")
        valinta = input("-> ")
    return valinta

# KOORDINAATTIEN HAKU

# def hae_koordinaatit(airport_name):
#    sql = "select latitude_deg, longitude_deg from airport where name = '" + airport_name + "'"
#    cursor = yhteys.cursor()
#    cursor.execute(sql)
#    result = cursor.fetchall()
#    return result

# MATKAN PITUUDEN LASKEMINEN

# def laske_välimatka(koordinaatit_1, koordinaatit_2):
#    result = geopy.distance.geodesic(koordinaatit_1, koordinaatit_2).km
#    return result

# LENTOMATKAN PITUUS (omaksi funktioksi?)

# lentokenttä_1 = lentokenttä, jossa oltiin viimeksi
# lentokenttä_2 = uusi lentokenttä, joka valittiin seuraavaksi matkakohteeksi
# koordinaatit_1 = hae_koordinaatit(lentokenttä_1)
# koordinaatit_2 = hae_koordinaatit(lentokenttä_2)
# välimatka = laske_välimatka(koordinaatit_1, koordinaatit_2)
# kuljettu_matka = + välimatka
# print(f"Kulkemasi matkan pituus: {kuljettu_matka:.0f} km")


# ______________________ PÄÄOHJELMA ______________________

yhteys = mysql.connector.connect(           # YHTEYS MYSQL
         host='localhost',
         port= 3306,
         database='tietovisa',
         user='root',
         password='salasana',
         autocommit=True
         )

while syöte != "0":
    mainmenu()                              # ALOITUSRUUTU
    käyttäjänimi = käyttäjänimenvalinta()   # KÄYTTÄJÄNIMEN KYSYNTÄ
    kotimaa = kotimaanvalinta()             # KOTIMAAN VALINTA
    valinta = end()
    if valinta == "0":
        break

