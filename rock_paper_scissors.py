#!/usr/bin/env python3.8
import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break # quits the game

    if user_input not in options: # checks if the input is in the list
        continue # if not, it continues the loop

    random_number = random.randint(0, 2) # generates a random number between 0 and 2
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number] # picks the option from the list
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors": # user wins
        print("You win!")
        user_wins += 1
        

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
        

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1

    else: # computer wins
        print("You lose!")
        computer_wins += 1

print(f"Your score: {user_wins}, Computer score: {computer_wins}")
print("Thanks for playing!")
print("Goodbye!")
        






