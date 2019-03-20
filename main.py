from classes import *
import random


# Deckcreation und Shuffle
deck = []
ablage = []
spieler01 = []
spieler02 = []

for i in range(1,11):
    deck.append(Card({"R"}, {i}))
    deck.append(Card({"G"}, {i}))
    deck.append(Card({"B"}, {i}))
    deck.append(Card({"Y"}, {i}))

#random.shuffle(deck)

# Test ob alle Objekte angekommen sind
# for i in range(0,40):
#     print(deck[i].color, deck[i].num)

print("---")
Spieler.hand.extend(deck[0:5])
del deck[0:5]


spieler02.extend(deck[0:5])
del deck[0:5]


ablage.extend(deck[0:1])
del deck[0]

