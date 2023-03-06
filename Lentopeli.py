import mysql.connector
import geopy.distance
import random

# ______________________ ALOITUSRUUTU ______________________
def mainmenu():
    print("____________________________________________________________________")
    print("  ")
    print("  ███████╗██╗░░░██╗██████╗░░█████╗░░█████╗░██████╗░██████╗░░█████╗░")
    print("  ██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗")
    print("  █████╗░░██║░░░██║██████╔╝██║░░██║██║░░██║██████╔╝██████╔╝███████║")
    print("  ██╔══╝░░██║░░░██║██╔══██╗██║░░██║██║░░██║██╔═══╝░██╔═══╝░██╔══██║")
    print("  ███████╗╚██████╔╝██║░░██║╚█████╔╝╚█████╔╝██║░░░░░██║░░░░░██║░░██║")
    print("  ╚══════╝░╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝░░╚═╝")
    print("  ████████╗██╗███████╗████████╗░█████╗░██╗░░░██╗██╗░██████╗░█████╗░")
    print("  ╚══██╔══╝██║██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██║██╔════╝██╔══██╗")
    print("  ░░░██║░░░██║█████╗░░░░░██║░░░██║░░██║╚██╗░██╔╝██║╚█████╗░███████║")
    print("  ░░░██║░░░██║██╔══╝░░░░░██║░░░██║░░██║░╚████╔╝░██║░╚═══██╗██╔══██║")
    print("  ░░░██║░░░██║███████╗░░░██║░░░╚█████╔╝░░╚██╔╝░░██║██████╔╝██║░░██║")
    print("  ░░░╚═╝░░░╚═╝╚══════╝░░░╚═╝░░░░╚════╝░░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝")
    print("            ALOITA PELI - ENTER            SULJE PELI - 0")
    print("____________________________________________________________________")
    syöte = input()
    while syöte != "" and syöte != "0":
        print("Virheellinen syöte!")
        print("Paina enter aloittaaksesi pelin.")
        print("Paina 0 lopettaaksesi ohjelman")
        syöte = input("-> ")
    return syöte

# ______________________ KÄYTTÄJÄNIMI ______________________
def käyttäjänimivalinta():
    print("   • Anna käyttäjänimesi •")
    print(" ")
    käyttäjänimi = input("-> ")
    print("____________________________________________________________________")
    return käyttäjänimi

# ____________________ ARPOO LENTOKENTÄN MAALLE ____________________
def etsimaanlentokenttä(maa):
    sql = "select airport.name from airport, maat where nimi = '" + str(maa) + "' and airport.iso_country = maat.iso_country and type = 'large_airport' order by rand() limit 1"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    length = len(tulos)
    # print(tulos)
    if length != 0:
        return tulos
    else: # JOS MAALLA EI OLE ISOA LENTOKENTTÄÄ, SE HAKEE KESKIKOKOISEN
        sql = "select airport.name from airport, maat where nimi = '" + str(maa) + "' and airport.iso_country = maat.iso_country and type = 'medium_airport' order by rand() limit 1"
        # print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
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
    print("  ")
    print("   • Olet maassa", ''.join(nykyinenmaa[0]), "Valitse minne haluat lentää! •")
    print("  ")
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
    print("____________________________________________________________________")
    print("  ")
    if valinta == "A":
        print("   • Lennetään lentokentälle", ''.join(valinta1[1]), ''.join(valinta1[0]), "•")
        valinta = valinta1
    elif valinta == "B":
        print("   • Lennetään lentokentälle", ''.join(valinta2[1]),''.join(valinta1[0]),"•")
        valinta = valinta2
    else:
        print("   • Lennetään lentokentälle", ''.join(valinta3[1]),''.join(valinta1[0]),"•")
        valinta = valinta3
    print("____________________________________________________________________")
    return valinta

# ______________________ KOTIMAAN VALINTA ______________________
def kotimaanvalinta(käyttäjänimi):
    print("  ")
    print("Tervetuloa pelaamaan Eurooppa Tietovisa peliä", käyttäjänimi, "!")
    print(" ")
    print("Tässä pelissä kierrät läpi kymmenen Euroopan maata")
    print("vastaten ei maihin liittyviin kysymyksiin.")
    print(" ")
    print("Aloita seikkailusi valitsemalla kotimaasi, josta aloitat pelin.")
    print("____________________________________________________________________")
    print("  ")
    arvotutmaat = arvokolmemaata()
    kerrat = 1
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
    print("____________________________________________________________________")
    print("  ")
    if valinta == "A":
        print("   • Kotimaaksi on valittu", ', '.join(valinta1),"•")
        valinta = valinta1
    elif valinta == "B":
        print("   • Kotimaaksi on valittu", ', '.join(valinta2),"•")
        valinta = valinta2
    else:
        print("   • Kotimaaksi on valittu", ', '.join(valinta3),"•")
        valinta = valinta3
    print("__________________________________________________________________")
    return valinta

# HAE VALITUN MAAN ID:
def hae_id(sijainti):

    sql = "select ID from maat where Nimi = '" + sijainti[0] + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    return result[0][0]

# VALITUN MAAN KYSYMYS PELAAJALLE:
def kysymys_pelaajalle(id, lennot):

    sql = "select ID, kysymys from vastaukset where paikka_id = '" + str(id) + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    kysymykset = cursor.fetchall()

    kysyttava_kysymys = random.choice(kysymykset)
    print("")
    print("Kysymys", lennot)
    print("")
    print(kysyttava_kysymys[1])
    print("")

    return kysyttava_kysymys[0]

# VASTAUSVAIHTOEHDOT PELAAJALLE:

def vastaus_vaihtoehdot(id):

    sql = "select oikein, väärin1, väärin2 from vastaukset where ID = '" + str(id) + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    ret = list(cursor.fetchall()[0])

    vastausvaihtoehdot = []
    vastausvaihtoehdot.append([ret[0], "oikein"])
    vastausvaihtoehdot.append([ret[1], "väärin"])
    vastausvaihtoehdot.append([ret[2], "väärin"])

    random.shuffle(vastausvaihtoehdot)

    vastausvaihtoehdot[0].append("A")
    vastausvaihtoehdot[1].append("B")
    vastausvaihtoehdot[2].append("C")

    for vastaus, paikkansapitavyys, kirjain in vastausvaihtoehdot:
        print(f"{kirjain}) {vastaus}")
    print("")

    return vastausvaihtoehdot

# PELAAJAN VASTAUS:
# palauttaa 0 jos vastaus oikein, -1 jos väärin

def anna_vastaus(vastaukset):

    pelaajan_syote = input("-> ").upper()

    while pelaajan_syote != "A" and  pelaajan_syote != "B" and pelaajan_syote != "C":
        print("")
        print("Virheellinen syöte! Valitse A, B tai C!")
        pelaajan_syote = input("-> ").upper()

    print("____________________________________________________________________")
    print("")
    for vastaus in vastaukset:
        if pelaajan_syote in vastaus:
            if vastaus[1] == "oikein":
                print("   Oikein!")
                return 0
            else:
                print("   Väärin meni!")
                return -1
    print("____________________________________________________________________")

# ______________________ PISTEFUNKTIO ______________________
def pisteidenlasku(pelaajan_vastaus, pisteet):
    if pelaajan_vastaus == 0:
        print("Oikein! Sait 80 pistettä!")
        pisteet = pisteet + 80
    else:
        print("Väärin meni. Menetit 20 pistettä.")
        pisteet = pisteet - 20
    print(f"Sinulla on nyt yhteensä {pisteet} pistettä.")
    return pisteet

# ______________________ LOPPURUUTU ______________________
def end():
    print("  ")
    print("   Onneksi olkoon", käyttäjänimi, "läpäisit pelin!")
    print("   Olet taas kotimaassasi", ', '.join(kotimaa))
    print("   Sait", pisteet, "pistettä!")
    print("  ")
    print("     PELAA UUDELLEEN - ENTER            SULJE PELI - 0")
    valinta = input("")
    while valinta != "" and valinta != "0":
        print("Virheellinen syöte!")
        valinta = input("")
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

# YHTEYS MYSQL:

syöte = 1
lennot = 1
pisteet = 0
kuljettu_matka = 0

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='root',
         password='keltainenKoira123',
         autocommit=True
         )

while syöte != "0":
    valinta = mainmenu()                    # ALOITUSRUUTU
    if valinta == "0":
        break
    käyttäjänimi = käyttäjänimivalinta()    # PALAUTTAA KÄYTTÄJÄNIMEN
    arvotutmaat = arvokolmemaata()          # PALAUTTAA 3 MAATA
    kotimaa = kotimaanvalinta(käyttäjänimi)             # PALAUTTAA KOTIMAAN
    nykyinenmaa = kotimaa
    while lennot < 11:
        nykyinenmaa = arvolentokenttä(nykyinenmaa)  # PALAUTTAA NYKYISEN MAAN
        id = hae_id(nykyinenmaa[0])                # HAKEE MAAN ID
        kysymys_id = kysymys_pelaajalle(id, lennot)        # HAKEE KYSYMYKSEN PELAAJALLE
        vastaukset = vastaus_vaihtoehdot(kysymys_id)  # HAKEE VASTAUSVAIHTOEHDOT PELAAJALLE
        pelaajan_vastaus = anna_vastaus(vastaukset)  # PELAAJA SYÖTTÄÄ VASTAUKSEN -> OIKEIN/VÄÄRIN
        pisteet = pisteidenlasku(pelaajan_vastaus, pisteet)
        lennot = lennot + 1
    valinta = end()
    if valinta == "0":
        break

