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

def paikka(icao):
    sql = "Select  from airport where ident = '" + icao + "'"
    #print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos
def username():
    print("Anna käyttäjänimesi:")
    käyttäjänimi = input("-> ")
    sql = "insert into käyttäjä(nimi,pisteet) values ('" + käyttäjänimi + "', 0)"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    yhteys.commit()
    print("Tervetuloa",käyttäjänimi)
    return käyttäjänimi

#def etäpisteet():



yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Suzu',
         autocommit=True
         )


käyttäjänimi = username()           # KÄYTTÄJÄNIMEN KYSYNTÄ JA SEN LISÄYS TIETOKANTAAN

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

