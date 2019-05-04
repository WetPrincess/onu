from gamelogic import *
import random

# Spieler und Bots Erstellung
# anzahlSpieler = int(input("Wie viele Spieler?"))
# anzahlBots = int(input("Wie viele Bots?"))
wins = {'True Bot 1':0, 'Dum Bot 1':0}

while True:
    anzahlSpieler = 0
    anzahlBots = 1
    spieler = []
    id = 0


    for anzahlSpieler in range(1, anzahlSpieler+1):
        spieler.append(Spieler({str(input("Spieler " + str(anzahlSpieler) + " wie heißt du? "))}))

    for anzahlBots in range(1, anzahlBots+1):
        spieler.append(Bot(("True Bot " + str(anzahlBots)),True))
    # Dum Bot added for testing
    spieler.append(Bot(("Dum Bot " + str(anzahlBots)), False))

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
    for ID in range(0, 2): # anzahlSpieler + anzahlBots):
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

    if ablage[-1].color == {"N"}:
        wuenschen(spieler, id, ablage)

    while True:

        if not isinstance(spieler[id], Bot):
            handzeigen(spieler, id, ablage)
            if kannablegen(spieler, id, ablage, deck):
                id = karteablegen(spieler, id, ablage, deck, None)
        else:
            print("Macht seinen Zug ...")
            if kannablegen(spieler,  id, ablage, deck):
                id = bot_karteablegen(spieler, ablage, id, deck, spieler[id].difficulty)

        if siegbedingung(spieler, id):
            break
            wins[spieler[id].ID] += 1
        deckvoll(deck, ablage)
        id = am_zug(spieler, id)

    if wins["True Bot 1"] == 1:
        print(wins)
        break