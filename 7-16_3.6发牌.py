import random

color = ['clubs', 'diamonds', 'hearts', 'spades']
number = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']
joker = ['JOKER1', 'JOKER2']
cards = [''.join([i, j]) for i in color for j in number]+joker
random.shuffle(cards)
player1 = cards[0:17]
player2 = cards[17:34]
player3 = cards[34:51]
surplus_cards = cards[51:54]
print('player1:', player1, len(player1))

print('player2:', player2, len(player2))
print('player3:', player3, len(player3))
print('surplus_cards:', surplus_cards)
