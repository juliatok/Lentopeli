import mysql.connector
import geopy.distance
import random

syöte = 1
pisteet = 300
kuljettu_matka = 0

# ______________________ ALOITUSRUUTU ______________________
def mainmenu():
    print("__________________________________________________________________")
    print("  ")
    print("███████╗██╗░░░██╗██████╗░░█████╗░░█████╗░██████╗░██████╗░░█████╗░")
    print("██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
    print("█████╗░░██║░░░██║██████╔╝██║░░██║██║░░██║██████╔╝██████╔╝███████║")
    print("██╔══╝░░██║░░░██║██╔══██╗██║░░██║██║░░██║██╔═══╝░██╔═══╝░██╔══██║")
    print("███████╗╚██████╔╝██║░░██║╚█████╔╝╚█████╔╝██║░░░░░██║░░░░░██║░░██║")
    print("╚══════╝░╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░░╚═╝")
    print("████████╗██╗███████╗████████╗░█████╗░██╗░░░██╗██╗░██████╗░█████╗░")
    print("╚══██╔══╝██║██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██║██╔════╝██╔══██╗")
    print("░░░██║░░░██║█████╗░░░░░██║░░░██║░░██║╚██╗░██╔╝██║╚█████╗░███████║")
    print("░░░██║░░░██║██╔══╝░░░░░██║░░░██║░░██║░╚████╔╝░██║░╚═══██╗██╔══██║")
    print("░░░██║░░░██║███████╗░░░██║░░░╚█████╔╝░░╚██╔╝░░██║██████╔╝██║░░██║")
    print("░░░╚═╝░░░╚═╝╚══════╝░░░╚═╝░░░░╚════╝░░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝")
    print("          ALOITA PELI - ENTER            SULJE PELI - 0")
    print("__________________________________________________________________")
    syöte = input()
    while syöte != "" and syöte != 0:
        print("Virheellinen syöte!")
        print("Paina enter aloittaaksesi pelin.")
        print("Paina 0 lopettaaksesi ohjelman")
        syöte = input("-> ")
    return syöte

# ______________________ KÄYTTÄJÄNIMI ______________________
def käyttäjänimivalinta():
    print("   Anna käyttäjänimesi:")
    käyttäjänimi = input("-> ")
    print("__________________________________________________________________")
    return käyttäjänimi

# ____________________ ARPOO LENTOKENTÄN MAALLE ____________________
def etsimaanlentokenttä(maa):
    sql = "select airport.name from airport, maat where nimi = '" + str(maa) +"' and airport.iso_country = maat.maakoodi and (type = 'large_airport' or type = 'medium_airport') order by rand() limit 1"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    #print(tulos)
    return tulos

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

# _________________ VALITSEE SEURAAVAN MAAN ______________________
def arvolentokenttä(nykyinenmaa): # ARPOO KOLME MAATA JA LENTOKENTTÄÄ MIHIN LENTÄÄ SEURAAVAKSI
    arvotutmaat = arvokolmemaata()
    kerrat = 1
    print("Olet maassa", ''.join(nykyinenmaa[0]), "Minne haluat lentää seuraavaksi:")
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
    print("__________________________________________________________________")
    return valinta

# ______________________ KOTIMAAN VALINTA ______________________
def kotimaanvalinta():
    arvotutmaat = arvokolmemaata()
    kerrat = 1
    print("   Hei", käyttäjänimi, "Valitse kotimaasi:")
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
    valinta = input("-> ").upper()
    while valinta != "A" and valinta != "B" and valinta != "C":
        print("Virheellinen syöte! Valitse A, B tai C!")
        valinta = input("-> ").upper()
    if valinta == "A":
        print("   Kotimaaksi on valittu", ', '.join(valinta1))
        valinta = valinta1
    elif valinta == "B":
        print("   Kotimaaksi on valittu", ', '.join(valinta2))
        valinta = valinta2
    else:
        print("   Kotimaaksi on valittu", ', '.join(valinta3))
        valinta = valinta3
    print("__________________________________________________________________")
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

# YHTEYS MYSQL
yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='assiponi',
         autocommit=True
         )

while syöte != "0":
    mainmenu()                              # ALOITUSRUUTU
    käyttäjänimi = käyttäjänimivalinta()    # KÄYTTÄJÄNIMEN KYSYNTÄ
    arvotutmaat = arvokolmemaata()          # ARPOO 3 MAATA
    kotimaa = kotimaanvalinta()             # KOTIMAAN VALINTA
    nykyinenmaa = kotimaa
    nykyinenmaa = arvolentokenttä(nykyinenmaa)
    valinta = end()
    if valinta == "0":
        break

