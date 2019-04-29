from classes import *
from gamelogic import *
import random

# Spieler und Bots Erstellung
# anzahlSpieler = int(input("Wie viele Spieler?"))
# anzahlBots = int(input("Wie viele Bots?"))

anzahlSpieler = 1
anzahlBots = 1
spieler = []
id = 0


for anzahlSpieler in range(1, anzahlSpieler+1):
    spieler.append(Spieler({anzahlSpieler}, {}))

for anzahlBots in range(1, anzahlBots+1):
    spieler.append(Bot({anzahlBots}, {}, {}))


# Deckcreation und Shuffle
deck = []
ablage = []

for i in range(1,11):
    deck.append(Card({"R"}, {i}))
    deck.append(Card({"G"}, {i}))
    deck.append(Card({"B"}, {i}))
    deck.append(Card({"Y"}, {i}))


random.shuffle(deck)

# Spieler bekommen karten
for i in range(0, anzahlSpieler + anzahlBots):
    spieler[i].hand.extend(deck[0:5])
    del deck[0:5]

ablage.extend(deck[0:1])
del deck[0]

# Spielablauf
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
