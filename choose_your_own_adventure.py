#!/usr/bin/env python3.8

name = input('What is your name? ')
print(f'Hello {name}! Welcome to this adventure.')

answer = input('You are on a dirt road. You come to a fork in the road. Do you want to go left or right? ').lower()

if answer == 'left':
    answer = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if answer == 'wait':
        print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?')
        answer = input('Type "red", "yellow", or "blue" to choose a door. ').lower()
        if answer == 'red':
            print('It is a room full of fire. Game Over.')
        elif answer == 'yellow':
            print('You found the treasure! You Win!')
        elif answer == 'blue':
            print('You enter a room of beasts. Game Over.')
    elif answer == 'swim':
        print('You get attacked by an angry trout. Game over.')
    else:
        print('You did not choose a valid option. You lose.')

elif answer == 'right':
    answer = input('You come to a bridge. There is a troll guarding the bridge. He asks you to pay a toll. Do you pay the troll? Type "yes" or "no". ').lower()
    if answer == 'yes':
        print('The troll takes your money and lets you pass. You arrive')
    elif answer == 'no':
        print('The troll attacks you. Game Over.')

else:
    print ('Not a valid answer. You lose.')

print('Thanks for playing!')