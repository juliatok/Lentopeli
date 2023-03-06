import mysql.connector
import geopy.distance

"""def tietovisa(maa):
    sql = "select nimi, kysymys, oikein, väärin1, väärin2 from maat, vastaukset where nimi = '" + maa + "' and maat.id = paikka_id"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def flight_game(icao):
    sql = "Select ident, name, municipality from airport where ident = '" + icao + "'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos"""

def username():
    print("Anna käyttäjänimesi:")
    käyttäjänimi = input("-> ")
    print("Tervetuloa",käyttäjänimi)
    return käyttäjänimi

#def etäpisteet():


# -- Tietokantaan lisäys --
def top5(käyttäjänimi,pisteet):
    """top5 = []
    haku = "select pisteet from käyttäjä"
    for rivi in haku:
        points = rivi[0]
        top5.append(points)
    if pisteet > top5[-1]:"""
    sql = "insert into käyttäjä(nimi,pisteet) values ('" + käyttäjänimi + "', '" + pisteet + "')"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    yhteys.commit()
    print("Tervetuloa", käyttäjänimi)
    return


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Suzu',
         autocommit=True
         )

käyttäjänimi = username()           # KÄYTTÄJÄNIMEN KYSYNTÄ JA SEN LISÄYS TIETOKANTAAN
pisteet = input("Anna pisteet:")
top5lista = top5(käyttäjänimi,pisteet)

'''icao = "EFHK"
paikka1 = paikka(icao)
paikka2 = paikka(icao)
input("choose one: A - close by airport, B - far away airport")'''
#etäpisteet ()

"""maa = input("Anna Maa:")
tulos = tietovisa(maa)
print(tulos)


icao = str(input("Anna ICAO-Koodi: "))
tulos = flight_game(icao)
for rivi in tulos:
    print(rivi[0],"-", rivi[2],"-", rivi[1])"""

