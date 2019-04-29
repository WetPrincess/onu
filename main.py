from classes import *
from gamelogic import *
import random

# Spieler und Bots Erstellung
# anzahlSpieler = int(input("Wie viele Spieler?"))
# anzahlBots = int(input("Wie viele Bots?"))

anzahlSpieler = 1
anzahlBots = 2
spieler = []
id = 0


for anzahlSpieler in range(1, anzahlSpieler+1):
    spieler.append(Spieler({anzahlSpieler}, {}))
    spieler[anzahlSpieler-1].ID = str(input("Spieler " + str(anzahlSpieler) + " wie heißt du?"))

for anzahlBots in range(1, anzahlBots+1):
    spieler.append(Bot({anzahlBots}, {}, {}))
    spieler[anzahlBots-1+anzahlSpieler].ID = ("Bot " + str(anzahlBots))


# Deckcreation und Shuffle
deck = []
ablage = []

for i in range(1,11):
    deck.append(Card({"R"}, {i}))
    deck.append(Card({"G"}, {i}))
    deck.append(Card({"B"}, {i}))
    deck.append(Card({"Y"}, {i}))

random.shuffle(spieler)
random.shuffle(deck)

# Spieler bekommen karten
for i in range(0, anzahlSpieler + anzahlBots):
    spieler[i].hand.extend(deck[0:5])
    del deck[0:5]

ablage.extend(deck[0:1])
del deck[0]

# Spielablauf

print()
print("Das Spiel beginnt!")
print(spieler[id].ID, "fängt an!")

while True:

        if isinstance(spieler[id], Bot) == False:
            handzeigen(spieler, id, ablage)
            if kannablegen(spieler, id, ablage, deck):
                karteablegen(spieler, id, ablage)
        else:
            print("Macht seinen Zug ...")
            if bot_kannablegen(spieler, ablage, deck, id):
                bot_karteablegen(spieler, ablage, id)

        siegbedingung(spieler, id)
        deckvoll(deck, ablage)
        id = am_zug(spieler, id)
