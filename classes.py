# Unsere Klassen werden hier deklariert

class Card:
    def __init__(self, color, num):
        self.color = color
        self.num = num


class Spieler:
    def __init__(self, ID, Hand):
        self.ID = None
        self.hand = []

class Bot(Spieler):
    def __init__(self, ID, Hand, IsBot):
        super().__init__(ID, Hand)
        self.isBot = True


