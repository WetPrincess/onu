import time

# Ist die Eingabe ein Integer?
def ist_zahl(karten_inp):
    try:
        int(karten_inp)
        return True
    except ValueError:
        return False


# Vergleich mit der Spielerhand
def handgroesse(karten_inp, spieler, id):
    if karten_inp <= len(spieler[id].hand) and karten_inp > 0:
        return True
    else:
        return False


# Spiellogik

# Zeigt aktuellen Spieler, Hand und Ablage
def handzeigen(spieler, id, ablage):
    print("Spieler", id + 1, "ist dran!")
    print("")
    for karte in range(0, len(spieler[id].hand)):
        print(karte + 1, spieler[id].hand[karte].color, spieler[id].hand[karte].num)

    print("")
    print("oberste karte auf dem ablagestapel: ")
    print(ablage[-1].color , ablage[-1].num)
    print("")
    
# Überprüfen ob eine Karte abgelegt werden kann
def kannablegen(spieler, id, ablage, deck):

    for card in range(0, len(spieler[id].hand)):
        if spieler[id].hand[card].color == ablage[-1].color or spieler[id].hand[card].num == ablage[-1].num:
            return True


    # Keine Karte kann abgelegt werden
    print("Spieler", id + 1, "kann keine Karte ablegen. Er muss eine ziehen!")
    spieler[id].hand.extend(deck[0:1])
    del deck[0]
    time.sleep(2)
    print("Spieler", id + 1, "neue Hand!")
    handzeigen(spieler, id, ablage)
    time.sleep(2)
    return False

# Spielerinput, dann wird die entsprechende Karte abgelegt
def karteablegen(spieler, id, ablage):
    while True:

        while True:
            karte_inp = input("Lege eine Karte ab:")
            if ist_zahl(karte_inp) and handgroesse(int(karte_inp), spieler, id):
                karte_inp = int(karte_inp) - 1
                break

        if spieler[id].hand[karte_inp].color == ablage[-1].color or spieler[id].hand[karte_inp].num == ablage[-1].num:

            ablage.extend(spieler[id].hand[karte_inp:karte_inp + 1])
            del spieler[id].hand[karte_inp]
            print(ablage[-1].color, ablage[-1].num)
            time.sleep(2)

            break

        else:
            print("Diese Karte kannst du nicht ablegen!")

# Die Siegbedingung wird überprüft, dann der Zug weitergegeben
def siegbedingung(spieler, id):

    if len(spieler[id].hand) == 0:
        print("Spieler", id + 1, "hat gewonnen!")

        quit()
    else:
        print("Nächster Zug!")
        print("##############################################################################################")
        print()
        time.sleep(2)



# Sind noch Karten auf dem Deck?

def deckvoll(deck, ablage):
    if len(deck) == 0:
        deck.extend(ablage[1:-1])
        del ablage[1:-1]
        print("Der Ablagestapel wurde ins Deck gemischt!")
        print()
        time.sleep(2)

# Zug wird weitergegeben
def am_zug(spieler, id):

    if id < len(spieler)-1:
        id += 1
    else:
        id = 0

    return id