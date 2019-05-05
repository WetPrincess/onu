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
        spieler[id].sprache(2)
        print(spieler[id].ID, "hat noch ", len(spieler[id].hand), "karten auf der Hand")
        print()
    #time.sleep(1)
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
            return plus_zwei(spieler,id, deck,ablage)

        elif spieler[id].hand[karte_inp].num == {"+4"}:

            spieler[id].ablegen_karte(spieler, id, ablage, karte_inp)
            return plus_vier(spieler, id, ablage, deck)

        elif spieler[id].hand[karte_inp].color == ablage[-1].color or spieler[id].hand[karte_inp].num == ablage[-1].num:

            spieler[id].ablegen_karte(spieler, id, ablage, karte_inp)
            # time.sleep(1)

            return id

        else:
            print("Diese Karte kannst du nicht ablegen!")


# Die Siegbedingung wird überprüft, dann der Zug weitergegeben

def siegbedingung(spieler, id):

    if len(spieler[id].hand) == 0:
        print(spieler[id].ID, "hat gewonnen!")
        if isinstance(spieler[id], Bot):
            spieler[id].sprache(3)
        return True
    else:
        print("Nächster Zug!")
        print("##############################################################################################")
        print()
        #time.sleep(1)



# Sind noch Karten auf dem Deck?

def deckvoll(deck, ablage):
    if len(deck) <= 4:
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

    return id

# SonderkartenFunktionen


def aussetzen(spieler, id):
    id = am_zug(spieler, id)
    print(spieler[id].ID, "muss aussetzen!")

    return id


def wechsel(spieler, id):
    print("Die Spielrichtung ändert sich!")
    for i in range(0, len(spieler)):
        spieler.append(spieler.pop((len(spieler)-1)-i))
    id = (len(spieler)-1)-id
    return id


def wuenschen(spieler, id, ablage):
    while True:
        if not isinstance(spieler[id], Bot):
            karte_inp = str(input("Wünsch dir eine Farbe. R, G, B, Y: "))
            if karte_inp == "R" or karte_inp == "B" or karte_inp == "Y" or karte_inp == "G":
                ablage[-1].color = {karte_inp}
                break
        else:
            ablage[-1].color = bot_farbprobe(spieler, id)[0][0]
            print(spieler[id].ID, "wünscht sich",ablage[-1].color )
            break


def plus_zwei(spieler, id, deck,ablage):
    id = aussetzen(spieler, id)
    deckvoll(deck, ablage)
    spieler[id].zieh_karte(2, spieler, id, deck)
    return id


def plus_vier(spieler, id, ablage,  deck):
    wuenschen(spieler, id, ablage)
    id = aussetzen(spieler, id)
    deckvoll(deck, ablage)
    spieler[id].zieh_karte(4, spieler, id, deck)
    return id


# Botfunktionen


# Kernfunktion mit einer Abfrage für "Dummen" und "Schlauen" Bot
def bot_karteablegen(spieler, ablage, id, deck, difficulty):
    if difficulty: # "True Bot", mit Spielflussrelativer Kartenwahl
        spieler[id].sprache(1)
        print(spieler[id].ID, "hat", len(spieler[id].hand), "Karten auf der Hand")
        print()
        id = karteablegen(spieler, id, ablage, deck, int(bot_kern(spieler, id, ablage)))
        print()
        #time.sleep(1)
        return id
    else: # Easy Bot, legt erstbeste Karte ab.
        print("I'm too dumb to exist! :(")
        for ablegen in range(0, len(spieler[id].hand)):
            if spieler[id].hand[ablegen].color == ablage[-1].color or spieler[id].hand[ablegen].num == ablage[-1].num\
                    or spieler[id].hand[ablegen].color == {"N"}:
                print(spieler[id].ID, "hat", len(spieler[id].hand), "Karten auf der Hand")
                print()
                id = karteablegen(spieler, id, ablage, deck, int(ablegen))
                print()
                #time.sleep(1)
                return id


# Botkern mit Kartenwahllogik und Regeln
def bot_kern(spieler, id, ablage):
    playable = []
    best_option = []
    for check in range(0, len(spieler[id].hand)):
        if spieler[id].hand[check].color == ablage[-1].color or\
                spieler[id].hand[check].num == ablage[-1].num or\
                spieler[id].hand[check].color == {"N"}:
            playable.append(check)
    print(playable)
    for check in playable:
        if spieler[id].hand[check].num == {"+4"} and (len(playable) == 1 or random.randint(1,4) == 1):
            best_option.append((check,1))
        elif spieler[id].hand[check].color == bot_farbprobe(spieler, id)[0][0] and\
                bot_farbprobe(spieler, id)[0][1] >= 2 and \
                len(spieler[bot_vorher_nachher(spieler, id)[0]].hand) > len(spieler[id].hand) and \
                len(spieler[bot_vorher_nachher(spieler, id)[0]].hand) != 1:
            best_option.append((check, 2))
            return check
        elif spieler[id].hand[check].num == {"X"} and \
                len(spieler[bot_vorher_nachher(spieler, id)[0]].hand) <= len(spieler[id].hand):
            best_option.append((check,3))
            return check

        elif spieler[id].hand[check].num == {"+2"} and\
                len(spieler[bot_vorher_nachher(spieler, id)[0]].hand) < len(spieler[id].hand):
            best_option.append((check,4))
            return check

        elif spieler[id].hand[check].num == {"<"} and\
                (len(spieler[bot_vorher_nachher(spieler, id)[0]].hand) < len(spieler[bot_vorher_nachher(spieler, id)[1]].hand) or\
                len(spieler[bot_vorher_nachher(spieler, id)[0]].hand) < 2 and\
                len(spieler[bot_vorher_nachher(spieler, id)[1]].hand) > len(spieler[bot_vorher_nachher(spieler, id)[0]].hand)):
            best_option.append((check,5))
            return check

        elif spieler[id].hand[check].num == ablage[-1].num and \
                (spieler[id].hand[check].color == bot_farbprobe(spieler,id)[0][0] or \
                spieler[id].hand[check].color == bot_farbprobe(spieler,id)[1][0] and \
                bot_farbprobe(spieler,id)[1][1] >= 2):
            best_option.append((check,6))
            return check
        else:
            best_option.append((check, 7))
    return playable[0]
    # print(best_option)
    # best_option.sort(key=lambda priority: priority[1])
    # print(best_option)
    # return best_option[0][0]


# Prüfung der Farbe mit den meisten Karten auf Hand
def bot_farbprobe(spieler, id):
    colors = [[{"R"},0],[{"B"},0],[{"Y"},0],[{"G"},0]]
    for check in range(0, len(spieler[id].hand)):
        if spieler[id].hand[check].color == {"R"}:
            colors[0][1] += 1
        if spieler[id].hand[check].color == {"B"}:
            colors[1][1] += 1
        if spieler[id].hand[check].color == {"Y"}:
            colors[2][1] += 1
        if spieler[id].hand[check].color == {"G"}:
            colors[3][1] += 1
    colors.sort(key=lambda colors: colors[1],reverse=True)
    # print(colors)
    return colors


# Ausgeben der Spieler-ID vor und nach Bot
def bot_vorher_nachher(spieler, id1):
    id2 = id1
    if id1 > 0:
        id2 -= 1
    else:
        id2 = -1
    id1 = am_zug(spieler, id1)
    return id1, id2
