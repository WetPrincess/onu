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


class Bot(Spieler):
    def __init__(self, ID,diff):
        super().__init__(ID)
        self.isBot = True
        self.difficulty = diff