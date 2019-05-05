import random
# Unsere Klassen werden hier deklariert


class Card:
    def __init__(self, color, num):
        self.color = color
        self.num = num


class Spieler:
    def __init__(self, ID):
        self.ID = ID
        self.hand = []

# Ziehfunktion
    def zieh_karte(self, anzahl, spieler, id, deck):
        for menge in range(anzahl):
            spieler[id].hand.extend(deck[0:1])
            del deck[0]
        print(spieler[id].ID, "zieht", anzahl, "mal!")

# Legefunktion
    def ablegen_karte(self, spieler, id, ablage, karte_inp):
        ablage.extend(spieler[id].hand[karte_inp:karte_inp + 1])
        del spieler[id].hand[karte_inp]
        print (spieler[id].ID, "spielt:")
        print(ablage[-1].color, ablage[-1].num)

# Zeigt aktuellen Spieler, Hand und Ablage
    def handzeigen(self, spieler, id, ablage):
        print(spieler[id].ID, "ist dran!")
        print()
        for karte in range(0, len(spieler[id].hand)):
            print(karte + 1, spieler[id].hand[karte].color, spieler[id].hand[karte].num)

        print()
        print("oberste karte auf dem ablagestapel: ")
        print(ablage[-1].color, ablage[-1].num)
        print()

class Bot(Spieler):
    def __init__(self, ID,diff):
        super().__init__(ID)
        self.isBot = True
        self.difficulty = diff

    def sprache(self, mode):
        lines = []
        with open("bot_lines.txt", "rt") as file:
            for line in file:
                lines.append(line)
        if mode == 1:
            print(lines[random.randint(1,6)])
        elif mode == 2:
            print(lines[random.randint(8, 11)])
        elif mode == 3:
            print(lines[random.randint(13, 16)])