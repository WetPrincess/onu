from gamelogic import *
import os
import random



# wins = {'Dumbo 1':0, 'True Bot 1':0}
# while True:

anzahlSpieler = 0
anzahlBots = 0
spieler = []
id = 0

# Spieler und Bots Erstellung
while True:
    anzahlSpieler = input("Wie viele Spieler? ")
    if ist_zahl(anzahlSpieler) and int(anzahlSpieler) < 11:
        anzahlSpieler = int(anzahlSpieler)
        break

while True:
    anzahlBots = input("Wie viele Bots? ")
    if ist_zahl(anzahlSpieler) and int(anzahlBots) < 11:
        anzahlBots = int(anzahlBots)
        break

# os.system("clear")

while True and anzahlBots > 0:
    print()
    print("Bots sind: ")
    print("1. Einfach")
    print("2. Klug")
    print()
    difficulty = input("welcher Schwierigkeitsgrad soll es sein? ")
    if int(difficulty) == 1:
        print("Du hast Einfach gewählt...")
        print()
        difficulty = False
        break
    if int(difficulty) == 2:
        print("Du hast den maximalen Intellekt gewählt...")
        print()
        difficulty = True
        break


for anzahlSpieler in range(1, anzahlSpieler+1):
    spieler.append(Spieler(str(input("Spieler " + str(anzahlSpieler) + " wie heißt du? "))))
    print()
    print("##############################################################################################")
    print()

for anzahlBots in range(1, anzahlBots+1):
    if difficulty == True:
        bot_name = random.choice(["SexMachine", "Killerbot", "Supremebeing", "Überbot", "Onubotextreme", "Fuckbot", "Terminationbot"])
    else:
       bot_name = random.choice(["Dumbo", "Idiot", "Whacko", "Retard", "Retardobot", "Shithead", "Redneck", "Cousinbot"])
    spieler.append(Bot((bot_name+ " " + str(anzahlBots) + str(random.randint(101, 9999))), difficulty))


# Deckcreation und Shuffle
deck = []
ablage = []

# Normiekarten generieren
for j in range(2):
    for i in range(0,10):
        deck.append(Card({"R"}, {i}))
        deck.append(Card({"G"}, {i}))
        deck.append(Card({"B"}, {i}))
        deck.append(Card({"Y"}, {i}))

# Sonderkarten generieren

# Aussetzen und Plus 2
for j in range(2):
    for i in ("X", "+2", "<"):
        deck.append(Card({"R"}, {i}))
        deck.append(Card({"G"}, {i}))
        deck.append(Card({"B"}, {i}))
        deck.append(Card({"Y"}, {i}))

# Farbwunsch und Plus 4
for i in range(4):
    deck.append(Card({"N"}, {"W"}))
    deck.append(Card({"N"}, {"+4"}))


random.shuffle(spieler)
random.shuffle(deck)

# Spieler bekommen karten
for ID in range(0, anzahlSpieler + anzahlBots):
    spieler[id].zieh_karte(5, spieler, ID, deck)

ablage.extend(deck[0:1])
del deck[0]
print("Erste Karte")
print(ablage[-1].color, ablage[-1].num)

# Spielablauf

print()
print("Das Spiel beginnt!")
print()
print(spieler[id].ID, "fängt an!")
print()
print("##############################################################################################")
print()

if ablage[-1].color == {"N"}:
    wuenschen(spieler, id, ablage)

while True:
    if not isinstance(spieler[id], Bot):
        spieler[id].handzeigen(spieler, id, ablage)
        if kannablegen(spieler, id, ablage, deck):
            id = karteablegen(spieler, id, ablage, deck, None)
    else:
        print(spieler[id].ID, "Macht seinen Zug ...")
        if kannablegen(spieler,  id, ablage, deck):
            id = bot_karteablegen(spieler, ablage, id, deck, spieler[id].difficulty)

    if siegbedingung(spieler, id):
        quit()
        # wins[spieler[id].ID] += 1
        # break
    deckvoll(deck, ablage)
    id = am_zug(spieler, id)
        # print(deck)
        # print(ablage)

    # if wins[spieler[id].ID] == 100000:
    #     print(wins)
    #
    #     break