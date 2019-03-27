from gamelogic import *

#Spielablauf

while True:

    k = reihe(k)
    handzeigen()
    if kannablegen():
        karteablegen()
    siegbedingung(k)
    deckvoll()
    print()
    print("######################################################################################################")
    print()