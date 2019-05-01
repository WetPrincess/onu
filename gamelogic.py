from classes import *
import random
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
    print("")
    for karte in range(0, len(spieler[id].hand)):
        print(karte + 1, spieler[id].hand[karte].color, spieler[id].hand[karte].num)

    print("")
    print("oberste karte auf dem ablagestapel: ")
    print(ablage[-1].color, ablage[-1].num)
    print("")


# Überprüfen ob eine Karte abgelegt werden kann

def kannablegen(spieler, id, ablage, deck):
    for card in range(0, len(spieler[id].hand)):
        if spieler[id].hand[card].color == ablage[-1].color or spieler[id].hand[card].num == ablage[-1].num\
                or spieler[id].hand[card].color == {"N"}:

            return True


    # Keine Karte kann abgelegt werden
    print(spieler[id].ID, "kann keine Karte ablegen!")
    spieler[id].zieh_karte(1, spieler, id, deck)
    # Ist aktueller Spieler ein Bot?
    if isinstance(spieler[id], Bot):
        print(spieler[id].ID, "hat noch ", len(spieler[id].hand), "karten auf der Hand")
        print()
    time.sleep(1)
    return False


# Spielerinput, dann wird die entsprechende Karte abgelegt

def karteablegen(spieler, id, ablage, deck, karte_inp):
    while True:
        while not isinstance(spieler[id], Bot) and True:
            karte_inp = input("Lege eine Karte ab: ")
            if ist_zahl(karte_inp) and handgroesse(int(karte_inp), spieler, id):
                karte_inp = int(karte_inp) - 1
                break

        if spieler[id].hand[karte_inp].num == {"X"}:

            spieler[id].ablegen_karte(spieler, id, ablage, karte_inp)
            return aussetzen(spieler, id)

        elif spieler[id].hand[karte_inp].num == {"<"}:

            spieler[id].ablegen_karte(spieler, id, ablage, karte_inp)
            return wechsel(spieler, id)

        elif spieler[id].hand[karte_inp].num == {"W"}:

            spieler[id].ablegen_karte(spieler, id, ablage, karte_inp)
            wuenschen(spieler, id, ablage)
            return id

        elif spieler[id].hand[karte_inp].num == {"+2"}:

            spieler[id].ablegen_karte(spieler, id, ablage, karte_inp)
            return plus_zwei(spieler,id, deck)

        elif spieler[id].hand[karte_inp].num == {"+4"}:

            spieler[id].ablegen_karte(spieler, id, ablage, karte_inp)
            return plus_vier(spieler, id, ablage, deck)

        elif spieler[id].hand[karte_inp].color == ablage[-1].color or spieler[id].hand[karte_inp].num == ablage[-1].num:

            spieler[id].ablegen_karte(spieler, id, ablage, karte_inp)
            time.sleep(1)

            return id

        else:print("Diese Karte kannst du nicht ablegen!")


# Die Siegbedingung wird überprüft, dann der Zug weitergegeben

def siegbedingung(spieler, id):

    if len(spieler[id].hand) == 0:
        print(spieler[id].ID, "hat gewonnen!")

        quit()
    else:
        print("Nächster Zug!")
        print("##############################################################################################")
        print()
        time.sleep(1)



# Sind noch Karten auf dem Deck?

def deckvoll(deck, ablage):
    if len(deck) == 0:
        deck.extend(ablage[1:-1])
        del ablage[1:-1]
        random.shuffle(deck)
        print("Der Ablagestapel wurde ins Deck gemischt!")
        print()


# Zug wird weitergegeben

def am_zug(spieler, id):
    if id < len(spieler)-1:
        id += 1
    else:
        id = 0
    print(spieler[id].ID, "ist dran!")

    return id

# SonderkartenFunktionen

def aussetzen(spieler, id):
    if int(id) < len(spieler) - 1:
        id += 1
    else:
        id = 0

    print(spieler[id].ID, "muss aussetzen!")
    return id

def wechsel(spieler, id):
    print("Die Spielrichtung ändert sich!")
    print(spieler[0].ID, spieler[1].ID, spieler[2].ID, spieler[3].ID, spieler[4].ID)
    print(id)
    for i in range(0, len(spieler)):
        spieler.append(spieler.pop((len(spieler)-1)-i))
    id = (len(spieler)-1)-id
    print(spieler[0].ID, spieler[1].ID, spieler[2].ID, spieler[3].ID, spieler[4].ID)
    print(id)
    return id

def wuenschen(spieler, id, ablage):
    while True:
        if not isinstance(spieler[id], Bot):
            karte_inp = str(input("Wünsch dir eine Farbe. R, G, B, Y: "))
            if karte_inp == "R" or karte_inp == "B" or karte_inp == "Y" or karte_inp == "G":
                ablage[-1].color = {karte_inp}
                break
        else:
            ablage[-1].color = random.choice([{"R"}, {"B"}, {"Y"}, {"G"}])
            print(spieler[id].ID, "wünscht sich",ablage[-1].color )
            break

def plus_zwei(spieler, id, deck):
    id = aussetzen(spieler, id)
    spieler[id].zieh_karte(2, spieler, id, deck)
    return id

def plus_vier(spieler, id, ablage,  deck):
    wuenschen(spieler, id, ablage)
    id = aussetzen(spieler, id)
    spieler[id].zieh_karte(4, spieler, id, deck)
    return id



# Bot

def bot_karteablegen(spieler, ablage, id, deck):
    for ablegen in range(0, len(spieler[id].hand)):
        if spieler[id].hand[ablegen].color == ablage[-1].color or spieler[id].hand[ablegen].num == ablage[-1].num\
                or spieler[id].hand[ablegen].color == {"N"}:
            print(spieler[id].ID, "hat", len(spieler[id].hand), "Karten auf der Hand")
            print()
            id = karteablegen(spieler, id, ablage, deck, int(ablegen))
            print()
            time.sleep(1)
            return id