import random
from classes import *
from main import *

k = 0

def reihe():

    #k += 1
    print("spieler", k+1 , "ist dran!")



#zeigt die hand des aktuellen spielers und ablage

def handzeigen():
    print("")
    for i in range(0, len(spieler[k].hand)):
        print(i + 1, spieler[k].hand[i].color, spieler[k].hand[i].num)

    print("")
    print("oberste karte auf dem ablagestapel: ")
    print(ablage[-1].color , ablage[-1].num)
    print("")

#Überprüfen ob eine Karte abgelegt werden kann

def kannablegen():
    ablegen = False
    for card in range(0, len(spieler[k].hand)):
        if spieler[k].hand[card].color == ablage[-1].color or spieler[k].hand[card].num == ablage[-1].num:
            ablegen = True



    if ablegen == False:
        print("Spieler", k+1 , "kann keine Karte ablegen. Er muss eine ziehen!")
        spieler[k].hand.extend(deck[0:1])
        del deck[0]
        handzeigen()

#Funktion um eine Karte aus der Hand auf die Ablage zu legen

def karteablegen():
    while True:
        ablegen = int(input("Lege eine Karte ab:"))
        ablegen -= 1

        if spieler[k].hand[ablegen].color == ablage[-1].color or spieler[k].hand[ablegen].num == ablage[-1].num:

            ablage.extend(spieler[k].hand[ablegen:ablegen + 1])
            del spieler[k].hand[ablegen]

            print(ablage[-1].color, ablage[-1].num)
            break

        else:
            print("Diese Karte kannst du nicht ablegen!")

def siegbedingung():
    if len(spieler[k].hand) == 0:
        print("Spieler", k+1 , "hat gewonnen!")
        quit()

def deckvoll():
    if len(deck) == 0:
        deck.extend(ablage[1:-1])
        del ablage[1:(-1)]


#Spielablauf

while True:
    reihe()
    handzeigen()
    kannablegen()
    karteablegen()
    siegbedingung()
    deckvoll()
