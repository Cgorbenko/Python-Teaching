#this is the goal

import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break



#
#import the random module

# Make A while loop that continues forever
    user_action = input("Enter a choice (rock, paper, scissors): ")
    #make a list of all the possible actions
    computer_action = random.choice(possible_actions)
    
    #Print what the computer chose and what the user chose. 
    #this below is an examble of the logic. Make more of these examples . 	
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")

    #ask user if they want to play again. 
    # chek if user says yes. If youser does not say yes, break
~                                                                                                    
~                
