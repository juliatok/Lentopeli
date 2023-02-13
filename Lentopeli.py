syöte = 1

def mainmenu():
    print("Paina enter aloittaaksesi pelin.")
    print("Paina 0 lopettaaksesi ohjelman")
    syöte = input("->")
    return syöte
def username():
    print("Anna käyttäjänimesi:")
    käyttäjänimi = input("->")
    return käyttäjänimi
def maanvalinta():
    print("Hei", käyttäjänimi, "Valitse kotimaasi:")
    print("A. Suomi B. Ruotsi C. Tanska")
    valinta = input("->")
    return valinta

mainmenu()
while syöte != "0":
    if syöte != "0":
        käyttäjänimi = username()
        maanvalinta()

