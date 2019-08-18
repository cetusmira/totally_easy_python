#section_092.py

import random

card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(card)

random.shuffle(card)
print(card)

print(random.choice(card))
