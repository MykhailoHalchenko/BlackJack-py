cards = [8, 38, 4, 56, 32, 22, 18, 0, 88]*4

import random
random.shuffle(cards)
print("Play in game")
count = 0
while True:
    choice = input('Will you take the card: ')
    if choice == 'y':
        current = cards.pop()
        print('You got a card %d' %current)
        count +=current
        if count > 21:
            print('You loser haha!')
            break
        elif count == 21:
            print('Great!')
            break
        else:
            print('You have a %d points' %count)
    elif choice == 'n':
        print('You have a %d points good luck!' %count)
        break
print('Game Over!')