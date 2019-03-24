import random
from classes import *
#from main import *


def arsch():
    if random.randint(0,1) == 1 :
        print("Du bist dran")
    else:
            pass

arsch()

def handzeigen():
    for i in range(0, len(spieler.hand)):
        print(i + 1, spieler.hand[i].color, spieler.hand[i].num)

    print("Oberste Karte auf dem Ablagestapel: ")
    print(ablage[-1].color , ablage[-1].num)


handzeigen()

def karteablegen():
    while True:
        ablegen = int(input("Lege eine Karte ab:"))
        ablegen -= 1
        if spieler.hand[ablegen].color == ablage[-1].color or spieler.hand[ablegen].num == ablage[-1].num:
            ablage.extend(spieler.hand[ablegen:ablegen + 1])
            del spieler.hand[ablegen]
            print(ablage[-1].color, ablage[-1].num)
            break
        else:
            print("Diese Karte kannst du nicht ablegen!")


karteablegen()