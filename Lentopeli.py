syöte = 1
pisteet = 300

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
    valinta = end()
    if valinta == "0":
        break

