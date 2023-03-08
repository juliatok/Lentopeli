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
    sql = "select airport.name, airport.id from airport, maat where nimi = '" + str(
        maa) + "' and airport.iso_country = maat.iso_country and type = 'large_airport' order by rand() limit 1"
    # print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    length = len(tulos)
    print(tulos)
    if length != 0:
        return tulos
    else:  # JOS MAALLA EI OLE ISOA LENTOKENTTÄÄ, SE HAKEE KESKIKOKOISEN
        sql = "select airport.name, airport.id from airport, maat where nimi = '" + str(
            maa) + "' and airport.iso_country = maat.iso_country and type = 'medium_airport' order by rand() limit 1"
        # print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        print(tulos)
        return tulos


# ______________________ ARPOO 3 MAATA ______________________


def arvokolmemaata():
    kerrat = 0
    arvotutmaat = []
    while kerrat != 3:
        numero = random.randint(1, 30)
        sql = "select Nimi from maat where ID = '" + str(numero) + "'"
        # print(sql)
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchall()
        for n in tulos:
            if n not in käydytmaat:
                if n not in arvotutmaat:
                    # print(n)
                    arvotutmaat.append(n)
                    kerrat = kerrat + 1
    return arvotutmaat


# _________________ VALITSEE SEURAAVAN MAAN ______________________


def arvolentokenttä(nykyinenmaa):  # ARPOO KOLME MAATA JA LENTOKENTTÄÄ MIHIN LENTÄÄ SEURAAVAKSI
    arvotutmaat = arvokolmemaata()
    kerrat = 1
    print("  ")
    print("   • Olet maassa", ''.join(nykyinenmaa[0]), "- Valitse minne haluaisit lentää! •")
    print("  ")
    for n in arvotutmaat:
        if kerrat == 1:
            kenttä = etsimaanlentokenttä(''.join(n))
            print(kenttä)
            print("A.", ''.join(n), "-", ''.join(map(str, kenttä[0])))
            kerrat = kerrat + 1
            valinta1 = [n, kenttä[0]]
        elif kerrat == 2:
            kenttä = etsimaanlentokenttä(''.join(n))
            print(kenttä)
            print("B.", ''.join(n), "-", ''.join(map(str, kenttä[0])))
            kerrat = kerrat + 1
            valinta2 = [n, kenttä[0]]
        else:
            kenttä = etsimaanlentokenttä(''.join(n))
            print(kenttä)
            print("C.", ''.join(n), "-", ''.join(map(str, kenttä[0])))
            kerrat = kerrat + 1
            valinta3 = [n, kenttä[0]]
    valinta = input("-> ").upper()
    while valinta != "A" and valinta != "B" and valinta != "C":
        print("Virheellinen syöte! Valitse A, B tai C!")
        valinta = input("-> ").upper()
    print("____________________________________________________________________")
    print("  ")
    if valinta == "A":
        print("   • Lennetään lentokentälle", ''.join(map(str, valinta1[1])), ''.join(valinta1[0]), "•")
        valinta = valinta1
    elif valinta == "B":
        print("   • Lennetään lentokentälle", ''.join(map(str, valinta1[1])), ''.join(valinta2[0]), "•")
        valinta = valinta2
    else:
        print("   • Lennetään lentokentälle", ''.join(map(str, valinta1[1])), ''.join(valinta3[0]), "•")
        valinta = valinta3
    print("____________________________________________________________________")
    return valinta


# ______________________ KOTIMAAN VALINTA ______________________


def kotimaanvalinta(käyttäjänimi):
    print("  ")
    print("Tervetuloa pelaamaan Eurooppa Tietovisa -peliä", käyttäjänimi, "!")
    print(" ")
    print("Tässä pelissä kierrät läpi kymmenen Euroopan maata")
    print("vastaten kussakin maassa maahan liittyvään tietovisa-kysymykseen.")
    print(" ")
    print("Aloita seikkailusi valitsemalla kotimaasi, josta aloitat pelin.")
    print("____________________________________________________________________")
    print("  ")
    arvotutmaat = arvokolmemaata()
    kerrat = 1
    for n in arvotutmaat:
        if kerrat == 1:
            print("A.", ', '.join(n))
            kerrat = kerrat + 1
            valinta1 = n
        elif kerrat == 2:
            print("B.", ', '.join(n))
            kerrat = kerrat + 1
            valinta2 = n
        else:
            print("C.", ', '.join(n))
            kerrat = kerrat + 1
            valinta3 = n
    valinta = input("-> ").upper()
    while valinta != "A" and valinta != "B" and valinta != "C":
        print("Virheellinen syöte! Valitse A, B tai C!")
        valinta = input("-> ").upper()
    print("____________________________________________________________________")
    print("  ")
    if valinta == "A":
        print("   • Kotimaaksi on valittu", ', '.join(valinta1), "•")
        valinta = valinta1
    elif valinta == "B":
        print("   • Kotimaaksi on valittu", ', '.join(valinta2), "•")
        valinta = valinta2
    else:
        print("   • Kotimaaksi on valittu", ', '.join(valinta3), "•")
        valinta = valinta3
    print("__________________________________________________________________")
    return valinta


# HAE RANDOM LENTOKENTTÄ KOTIMAASTA (matkan pituuden laskuun - ei näy pelissä):


def hae_kotikentta(valittu_kotimaa):

    count = 0

    while count <= 1:
        sql = "select airport.name from airport, maat " \
              "where nimi = ""'" + str(valittu_kotimaa) + "' " \
                "and airport.iso_country = maat.iso_country order by rand() limit 1"
        cursor = yhteys.cursor()
        cursor.execute(sql)
        arvottu_kotikentta = cursor.fetchall()

        return arvottu_kotikentta[0]


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
    ret = list(cursor.fetchall()[0])  # tekee listan tuplesta

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


# PELAAJAN VASTAUS (palauttaa 0 jos vastaus oikein, -1 jos väärin):


def anna_vastaus(vastaukset):

    pelaajan_syote = input("-> ").upper()

    while pelaajan_syote != "A" and pelaajan_syote != "B" and pelaajan_syote != "C":
        print("")
        print("Virheellinen syöte! Valitse A, B tai C!")
        pelaajan_syote = input("-> ").upper()

    print("____________________________________________________________________")
    print("")

    for vastaus in vastaukset:
        if pelaajan_syote in vastaus:
            if vastaus[1] == "oikein":
                return 0
            else:
                return -1

    print("____________________________________________________________________")


# ______________________ PISTEFUNKTIO ______________________


def pisteidenlasku(pelaajan_vastaus, pisteet):
    if pelaajan_vastaus == 0:
        print("Oikein! Sait 80 pistettä!")
        pisteet = pisteet + 80
    else:
        print("Väärin meni! Menetit 20 pistettä.")
        pisteet = pisteet - 20
    print(f"Sinulla on nyt yhteensä {pisteet} pistettä.")
    return pisteet


# HAKEE EDELLISEN JA NYKYISEN LENTOKENTÄN:


def edellinen_nykyinen_lentokentta(kentat_lista):

    edellinen = kentat_lista[-2][0]
    nykyinen = kentat_lista[-1][0]

    return edellinen, nykyinen


# HAKEE LENTOKENTÄN KOORDINAATIT:


def hae_koordinaatit(airport_name):

    sql = "select latitude_deg, longitude_deg from airport where name = '" + airport_name + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    return result


# LASKEE EDELLISEN JA NYKYISEN LENTOKENTÄN VÄLIMATKAN:


def laske_valimatka(koordinaatit1, koordinaatit2):

    print(f"Koordinaatit: {koordinaatit1}, {koordinaatit2}")
    valimatka = geopy.distance.geodesic(koordinaatit1, koordinaatit2).km

    return valimatka


# ______________________ LOPPURUUTU ______________________


def end():
    print("  ")
    print("   Onneksi olkoon", käyttäjänimi, "läpäisit pelin!")
    print("   Olet taas kotimaassasi", ', '.join(kotimaa))
    print("   Sait", pisteet, "pistettä!")
    print("  ")
    print(f"   Lensit pelin aikana yhteensä {kuljettu_matka:.0f} km")
    print("")
    print("     PELAA UUDELLEEN - ENTER            SULJE PELI - 0")
    valinta = input("")
    while valinta != "" and valinta != "0":
        print("Virheellinen syöte!")
        valinta = input("")
    return valinta


# ______________________ PÄÄOHJELMA ______________________

syöte = 1

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='m!näk00d44n',
    autocommit=True
)

while syöte != "0":

    lennot = 1
    pisteet = 0
    kuljettu_matka = 0

    valinta = mainmenu()  # ALOITUSRUUTU
    käydytmaat = []  # LISTAA KAIKKI MAAT JOSSA PELAAJA ON KÄYNYT
    kaydyt_lentokentat = []

    if valinta == "0":

        break

    käyttäjänimi = käyttäjänimivalinta()  # PALAUTTAA KÄYTTÄJÄNIMEN

    arvotutmaat = arvokolmemaata()  # PALAUTTAA 3 MAATA

    kotimaa = kotimaanvalinta(käyttäjänimi)  # PALAUTTAA KOTIMAAN
    kotimaa_lentokentta = hae_kotikentta(kotimaa[0])
    käydytmaat.append(kotimaa)
    kaydyt_lentokentat.append(kotimaa_lentokentta)
    nykyinenmaa = kotimaa

    while lennot < 11:

        nykyinenmaa = arvolentokenttä(nykyinenmaa)  # PALAUTTAA NYKYISEN MAAN
        käydytmaat.append(nykyinenmaa[0])
        kaydyt_lentokentat.append(nykyinenmaa[1])

        id = hae_id(nykyinenmaa[0])
        kysymys_id = kysymys_pelaajalle(id, lennot)
        vastaukset = vastaus_vaihtoehdot(kysymys_id)
        pelaajan_vastaus = anna_vastaus(vastaukset)

        pisteet = pisteidenlasku(pelaajan_vastaus, pisteet)

        edellinen, nykyinen = edellinen_nykyinen_lentokentta(kaydyt_lentokentat)
        koordinaatit_1 = hae_koordinaatit(edellinen)
        koordinaatit_2 = hae_koordinaatit(nykyinen)
        valimatka = laske_valimatka(koordinaatit_1, koordinaatit_2, )

        lennot = lennot + 1
        kuljettu_matka += valimatka

    valinta = end()

    if valinta == "0":

        break