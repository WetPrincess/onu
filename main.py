from classes import *


# =============
# Deckcreation
# =============

deck = []

for cards in range(1,11):
    deck.append(Card({"Red"}, {cards}))
    deck.append(Card({"Green"}, {cards}))
    deck.append(Card({"Blue"}, {cards}))
    deck.append(Card({"Yellow"}, {cards}))

# Test ob alle Objekte angekommen sind
for printout in range(0,40):
    print(deck[printout].color, deck[printout].num)

