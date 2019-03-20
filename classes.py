# Unsere Klassen werden hier deklariert

class Card:
    def __init__(self, color, num):
        self.color = color
        self.num = num


class Spieler:


    def __init__(self, id, hand):
        self.id = None
        self.hand = []

class Bot(Spieler):
    pass