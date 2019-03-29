import time

# Ist die Eingabe eine Zahl?
def ist_zahl(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# Vergleich mit der Spielerhand
def handgroesse(ablegen, spieler, k):
    if ablegen <= len(spieler[k].hand) and ablegen > 0:
        return True
    else:
        return False


# Spiellogik

# Wer ist gerade am Zug
def reihe(spieler, k):

    if k < len(spieler)-1:
        k += 1
    else:
        k = 0
    print("Spieler", k + 1, "ist dran!")

    return k


# zeigt die hand des aktuellen spielers und ablage
def handzeigen(spieler, ablage, k):
    print("")
    for i in range(0, len(spieler[k].hand)):
        print(i + 1, spieler[k].hand[i].color, spieler[k].hand[i].num)

    print("")
    print("oberste karte auf dem ablagestapel: ")
    print(ablage[-1].color , ablage[-1].num)
    print("")

# Überprüfen ob eine Karte abgelegt werden kann
def kannablegen(spieler, ablage, deck, k):
    for card in range(0, len(spieler[k].hand)):
        if spieler[k].hand[card].color == ablage[-1].color or spieler[k].hand[card].num == ablage[-1].num:
            return True


    # Keine Karte kann abgelegt werden
    print("Spieler", k + 1, "kann keine Karte ablegen. Er muss eine ziehen!")
    spieler[k].hand.extend(deck[0:1])
    del deck[0]
    time.sleep(2)
    print("Spieler", k+1 , "neue Hand!")
    handzeigen(spieler, ablage, k)
    time.sleep(2)
    return False

# Spielerinput, dann wird die entsprechende Karte abgelegt
def karteablegen(spieler, ablage, k):
    while True:

        while True:
            ablegen = input("Lege eine Karte ab:")
            if ist_zahl(ablegen) and handgroesse(int(ablegen), spieler, k):
                ablegen = int(ablegen)
                ablegen -= 1
                break

        if spieler[k].hand[ablegen].color == ablage[-1].color or spieler[k].hand[ablegen].num == ablage[-1].num:

            ablage.extend(spieler[k].hand[ablegen:ablegen + 1])
            del spieler[k].hand[ablegen]
            print(ablage[-1].color, ablage[-1].num)
            time.sleep(2)
            break

        else:
            print("Diese Karte kannst du nicht ablegen!")

# Die Siegbedingung wird überprüft, dann der Zug weitergegeben
def siegbedingung(spieler, k):

    if len(spieler[k].hand) == 0:
        print("Spieler", k + 1, "hat gewonnen!")
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