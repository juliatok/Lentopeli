# import mysql.connector
# import geopy.distance

syöte = 1
pisteet = 300
kuljettu_matka = 0

# ALOITUSRUUTU
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

# KÄYTTÄJÄNIMEN SYÖTTÖ
def username():
    print("Anna käyttäjänimesi:")
    käyttäjänimi = input("-> ")
    return käyttäjänimi

# KOTIMAAN VALINTA
def maanvalinta():
    print("Hei", käyttäjänimi, "Valitse kotimaasi:")
    print("A. Suomi B. Ruotsi C. Tanska")
    valinta = input("-> ")
    while valinta != "A" and valinta != "B" and valinta != "C":
        print("Virheellinen syöte!")
        print("Valitse kotimaasi:")
        print("A. Suomi B. Ruotsi C. Tanska")
        valinta = input("-> ")
    return valinta

# LOPPURUUTU
def end():
    print("Onneksi olkoon", käyttäjänimi, "läpäisit pelin!")
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
#    sql = "select latitude_deg, longitude_deg from airport where name = '" + name + "'"
#    cursor = yhteys.cursor()
#    cursor.execute(sql)
#    result = cursor.fetchall()
#    return result

# MATKAN PITUUDEN LASKEMINEN

# def laske_välimatka(koordinaatit_1, koordinaatit_2):
#    result = geopy.distance.geodesic(koordinaatit_1, koordinaatit_2).km
#    return result


# PÄÄOHJELMA

# YHTEYS MYSQL

# yhteys = mysql.connector.connect(
#          host='127.0.0.1',
#          port= 3306,
#          database='-',
#          user='-',
#          password='-',
#          autocommit=True
#          )

while syöte != "0":
    mainmenu()
    käyttäjänimi = username()
    maanvalinta()

# LENTOMATKAN PITUUS (omaksi funktioksi?)

# lentokenttä_1 = lentokenttä, jossa oltiin viimeksi
# lentokenttä_2 = uusi lentokenttä, joka valittiin seuraavaksi matkakohteeksi
# koordinaatit_1 = hae_koordinaatit(lentokenttä_1)
# koordinaatit_2 = hae_koordinaatit(lentokenttä_2)
# välimatka = laske_matka(koordinaatit_1, koordinaatit_2)
# kuljettu_matka = + välimatka
# print(f"Kulkemasi matkan pituus: {kuljettu_matka} km")

    valinta = end()
    if valinta == "0":
        break

