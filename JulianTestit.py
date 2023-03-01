import mysql.connector
import geopy.distance
import random

"""kuljettu_matka = 0


def hae_koordinaatit(airport_name):
    sql = "select latitude_deg, longitude_deg from airport where name = '" + airport_name + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def laske_välimatka(koordinaatit1, koordinaatit2):
    #    print(koordinaatit_1)
    #    print(koordinaatit_2)
    välimatka = geopy.distance.geodesic(koordinaatit_1, koordinaatit_2).km
    print(f"Välimatka: {välimatka:.0f} km")
    return välimatka"""


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='m!näk00d44n',
    autocommit=True
)

"""lentokenttä_1 = "Helsinki Vantaa Airport"
lentokenttä_2 = "London Heathrow Airport"
koordinaatit_1 = hae_koordinaatit(lentokenttä_1)
koordinaatit_2 = hae_koordinaatit(lentokenttä_2)
välimatka = laske_välimatka(koordinaatit_1, koordinaatit_2)
kuljettu_matka = + välimatka
print(f"Kulkemasi matkan pituus yhteensä: {kuljettu_matka:.0f} km")"""

# HAE VASTAUKSET TIETOKANNASTA:

lennot = 0


def hae_id(valinta):

    sql = "select ID from maat where Nimi = '" + valinta + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    return result[0][0]

def kysymys_pelaajalle(id):

    sql = "select ID, kysymys from vastaukset where paikka_id = '" + str(id) + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    kysymykset = cursor.fetchall()

    kysyttava_kysymys = random.choice(kysymykset)
    print(kysyttava_kysymys[1])
    print("")

    return kysyttava_kysymys[0]


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


def anna_vastaus(vastaukset):

    pelaajan_syote = input("-> ").upper()

    while pelaajan_syote != "A" and  pelaajan_syote != "B" and pelaajan_syote != "C":
        print("")
        print("Virheellinen syöte! Valitse A, B tai C!")
        pelaajan_syote = input("-> ").upper()

    for vastaus in vastaukset:
        if pelaajan_syote in vastaus:
            if vastaus[1] == "oikein":
                print("")
                print("Oikein!")
            else:
                print("")
                print("Väärin meni!")

    return


while lennot < 1:
    valinta = "Iso-Britannia"
    id = hae_id(valinta)
    kysymys = kysymys_pelaajalle(id)
    vastaukset = vastaus_vaihtoehdot(kysymys)
    pelaajan_vastaus = anna_vastaus(vastaukset)

    lennot = lennot + 1



# anna vastausvaihtoehdot (random järjestys - A), B), C))

# käyttäjä syöttää vastauksens

# jos väärin - virheellinen syöte

# kun vastaus tietokannassa indeksissä 0 - oikein
# muuten väärin

# (pisteet)
# (seuraavat maa vaihtoehdot)
