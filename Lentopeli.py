syöte = 1
pisteet = 300

# ALOITUSRUUTU
def mainmenu():
    print("Paina enter aloittaaksesi pelin.")
    print("Paina 0 lopettaaksesi ohjelman")
    syöte = input("->")
    return syöte

# KÄYTTÄJÄNIMEN SYÖTTÖ
def username():
    print("Anna käyttäjänimesi:")
    käyttäjänimi = input("->")
    return käyttäjänimi

# KOTIMAAN VALINTA
def maanvalinta():
    print("Hei", käyttäjänimi, "Valitse kotimaasi:")
    print("A. Suomi B. Ruotsi C. Tanska")
    valinta = input("->")
    return valinta

# LOPPURUUTU
def end():
    print("Onneksi olkoon", käyttäjänimi, "läpäisit pelin!")
    print("Sait", pisteet, "pistettä!")
    print("Paina 1 palataksesi päävalikkoon")
    print("Paina 0 lopettaaksesi ohjelman")
    valinta = input("->")
    while valinta != "1" and valinta != "0":
        print("Virheellinen syöte!")
        print("Paina 1 palataksesi päävalikkoon")
        print("Paina 0 lopettaaksesi ohjelman")
        valinta = input("->")
    return valinta

# PÄÄOHJELMA
while syöte != "0":
    mainmenu()
    käyttäjänimi = username()
    maanvalinta()
    valinta = end()
    if valinta == "0":
        break

