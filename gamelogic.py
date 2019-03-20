from main import *
import random

def ersterSpielerDerDasSpielEroeffnet():
    if random.randint(0, 1) == 1:
        print("Du bist Dran")
    else:
        pass


def handZeigenSpieler01():
    print("Deine Hand:")
    for i in range(0,len(spieler01)):
        print(i+1, spieler01[i].color, spieler01[i].num)

    # Eine Karte vom Deck offen auf den Ablagestapel legen
    print("Oberste Karte auf dem Ablagestapel:")
    ablage.extend(deck[0:1])
    del deck[0]
    print(ablage[-1].color, ablage[-1].num)



