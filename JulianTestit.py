import mysql.connector
import geopy.distance

kuljettu_matka = 0


def hae_koordinaatit(airport_name):
    sql = "select latitude_deg, longitude_deg from airport where name = '" + airport_name + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def laske_välimatka(koordinaatit1, koordinaatit2):
    print(koordinaatit_1)
    print(koordinaatit_2)
    result = geopy.distance.geodesic(koordinaatit_1, koordinaatit_2).km
    return result

yhteys = mysql.connector.connect(
          host='127.0.0.1',
          port= 3306,
          database='flight_game',
          user='root',
          password='m!näk00d44n',
          autocommit=True
          )

lentokenttä_1 = "Dubai International Airport"
lentokenttä_2 = "Heathrow Airport"
koordinaatit_1 = hae_koordinaatit(lentokenttä_1)
koordinaatit_2 = hae_koordinaatit(lentokenttä_2)
välimatka = laske_välimatka(koordinaatit_1, koordinaatit_2)
print(välimatka)
kuljettu_matka = + välimatka
print(f"Kulkemasi matkan pituus: {kuljettu_matka:.0f} km")

# HAE VASTAUKSET TIETOKANNASTA:

# maa = seuraava valittu maa

# hae (random) kysymys 1 tai kysymys 2

# anna vastausvaihtoehdot (random järjestys - A), B), C))

# käyttäjä syöttää vastauksen

# jos väärin - virheellinen syöte

# kun vastaus tietokannassa indeksissä 0 - oikein
# muuten väärin

# (pisteet)
# (seuraavat maa vaihtoehdot)
