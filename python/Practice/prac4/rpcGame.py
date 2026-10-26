"""
ROCK PAPER SCISSOR GAME
1-input from user
2 - random choice for computer
3 - compare choices
4 - declare winner
"""

import random
items = ["rock", "paper", "scissor"]
def get_user_choice():
    userInput = input("Enter your choice (rock, paper, scissors): ").lower()
    while userInput not in items :
        print("invalid choice, please try again.")
        userInput = input("Enter your choice (rock, paper, scissors): ").lower()
    return userInput

def get_computer_choice():
    choice = random.choice(items)
    return choice

def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        print("its a tie")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    determine_winner(user_choice, computer_choice)
    play_again = input("Do you want to play again? (y/n): ").lower()
    play_list = ["y", "n"]
    while play_again not in play_list:
        print("Invalid input, please enter 'y' or 'n'.")
        play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "n":
        print("Thanks for playing!")
        break




