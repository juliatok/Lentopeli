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

def kysymys(sijainti):
     sql = "select kysymys from vastaukset where paikka_id = '" + sijainti + "'"
     cursor = yhteys.cursor()
     cursor.execute(sql)
     kysymykset = cursor.fetchall()
     kysyttava_kysymys = random.choice(kysymykset)
     for k in kysyttava_kysymys:
         print(k)


def vastaus_vaihtoehdot(sijainti):
    sql = "select oikein, väärin1, väärin2 from vastaukset where paikka_id = '" + sijainti + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    vastausvaihtoehdot = cursor.fetchall()
    print(vastausvaihtoehdot)
    return vastausvaihtoehdot

def kysymys_vastausvaihtoehdot_pelaajalle(kysymys, vastaukset):
    if kysymys == kysymys[0]:
            print(vastaukset[0])
    else:
            print(vastaukset[1])
    return

while lennot < 1:
    paikka_id = "1"
    kysymys = kysymys(paikka_id)
    vastaukset = vastaus_vaihtoehdot(paikka_id)
    lennot = lennot + 1



# anna vastausvaihtoehdot (random järjestys - A), B), C))

# käyttäjä syöttää vastauksens

# jos väärin - virheellinen syöte

# kun vastaus tietokannassa indeksissä 0 - oikein
# muuten väärin

# (pisteet)
# (seuraavat maa vaihtoehdot)
