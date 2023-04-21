#Tymoteusz Maj
#Github: Xeraoo

import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    user_choice = input("Choose rock, paper or scissors: ")
    user_choice = user_choice.lower()
    print("You chose", user_choice)
    print("Computer chose", computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print("You win!")
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You win!")
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("You win!")
    else:
        print("Computer wins!")

while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break