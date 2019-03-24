# Unsere Klassen werden hier deklariert

class Card:
    def __init__(self, color, num):
        self.color = color
        self.num = num

class spieler:
    def __init__(self, ID, Hand):
        self.ID = None
        self.hand = []

class Bot(spieler):
    pass