from classes import *
import random


# Deckcreation und Shuffle
deck = []
spieler01 = []
spieler02 = []

for i in range(1,11):
    deck.append(Card({"Red"}, {i}))
    deck.append(Card({"Green"}, {i}))
    deck.append(Card({"Blue"}, {i}))
    deck.append(Card({"Yellow"}, {i}))

# random.shuffle(deck)


# Test ob alle Objekte angekommen sind
# for i in range(0,40):
#     print(deck[i].color, deck[i].num)

print("---")
spieler01.extend(deck[0:5])
del deck[0:5]
print(spieler01[0].color)

spieler02.extend(deck[0:5])
del deck[0:5]
print(spieler02[0].color)
