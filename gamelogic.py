import random
from classes import *
from main import *


def arsch():
    if random.randint(0,1) == 1 :
        print("Du bist dran")
    else:
            pass

arsch()

def handzeigen():
    for i in range(0,len(Spieler.hand)):
        print(i+1 , Spieler.hand[i].color , Spieler.hand[i].num)

    print("Oberste Karte auf dem Ablagestapel: ")
    print(ablage[-1].color , ablage[-1].num)


handzeigen()

def karteablegen():
    while True:
        ablegen = int(input("Lege eine Karte ab:"))
        ablegen -= 1
        if Spieler.hand[ablegen].color == ablage[-1].color or Spieler.hand[ablegen].num == ablage[-1].num:
            ablage.extend(Spieler.hand[ablegen:ablegen + 1])
            del Spieler.hand[ablegen]
            print(ablage[-1].color, ablage[-1].num)
            break
        else:
            print("Diese Karte kannst du nicht ablegen!")


karteablegen()