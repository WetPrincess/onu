from random import *
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
    #os.system('clear')

    print("")
    for i in range(0, len(spieler[k].hand)):
        print(i + 1, spieler[k].hand[i].color, spieler[k].hand[i].num)

    print("")
    print("oberste karte auf dem ablagestapel: ")
    print(ablage[-1].color, ablage[-1].num)
    print("")

# Überprüfen ob eine Karte abgelegt werden kann


def kannablegen(spieler, ablage, deck, k):
    ablegen = False
    for card in range(0, len(spieler[k].hand)):
        if spieler[k].hand[card].color == ablage[-1].color or spieler[k].hand[card].num == ablage[-1].num:
            return True



    if ablegen == False:
        print("Spieler", k + 1, "kann keine Karte ablegen. Er muss eine ziehen!")
        spieler[k].hand.extend(deck[0:1])
        del deck[0]
        # input("Weiter!")
        # print()
        # print("Spieler", k+1 , "neue Hand!")
        # input("Weiter!")
        print()
        input("Weiter!")
        handzeigen(spieler, ablage, k)
        return False

# Funktion um eine Karte aus der Hand auf die Ablage zu legen

def karteablegen(spieler, ablage, k):
    while True:

        while True:
            ablegen = int(input("Lege eine Karte ab:"))
            ablegen -= 1
            if ablegen < len(spieler[k].hand):
                break

        if spieler[k].hand[ablegen].color == ablage[-1].color or spieler[k].hand[ablegen].num == ablage[-1].num:

            ablage.extend(spieler[k].hand[ablegen:ablegen + 1])
            del spieler[k].hand[ablegen]

            print(ablage[-1].color, ablage[-1].num)
            break

        else:
            print("Diese Karte kannst du nicht ablegen!")

#Die Siegbedingung wird überprüft, dann der Zug weitergegeben

def siegbedingung(spieler, k):

    if len(spieler[k].hand) == 0:
        print("Spieler", k + 1, "hat gewonnen!")
        quit()
    else:
        print("Nächster Zug!")
        print("##############################################################################################")
        print()


#Sind noch Karten auf dem Deck?
def deckvoll(deck, ablage):
    if len(deck) == 0:
        deck.extend(ablage[1:-1])
        del ablage[1:-1]
        random.shuffle(deck)
        print("Der Ablagestapel wurde ins Deck gemischt!")
        print()


# Bot

def bot_kannablegen(spieler, ablage, deck, k):
    ablegen = False
    for card in range(0, len(spieler[k].hand)):
        if spieler[k].hand[card].color == ablage[-1].color or spieler[k].hand[card].num == ablage[-1].num:
            return True

    if ablegen == False:
        print("Spieler", k + 1, "kann keine Karte ablegen. Er muss eine ziehen!")
        spieler[k].hand.extend(deck[0:1])
        del deck[0]
        input("Weiter!")
        print()
        # print("Spieler", k+1 , "neue Hand!")
        # input("Weiter!")
        return False


def bot_karteablegen(spieler, ablage, k):
    for ablegen in range(0, len(spieler[k].hand)):
        if spieler[k].hand[ablegen].color == ablage[-1].color or spieler[k].hand[ablegen].num == ablage[-1].num:
            ablage.extend(spieler[k].hand[ablegen:ablegen + 1])
            del spieler[k].hand[ablegen]
            print("Spieler", k+1 , "hat noch ", len(spieler[k].hand), "karten auf der Hand")
            break

