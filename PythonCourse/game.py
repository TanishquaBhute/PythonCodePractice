import random
import sys


def get_user_choice(options):
    print(f"Choices :{options}")
    user_choice = input("Enter your choice :")
    if user_choice in options:
        return user_choice
    else:
        print("Wrong Choice")

        #sys.exit()


def get_computer_choice(options):
    computer_choice = random.choice(options)
    print(f"Computer choice : {computer_choice}")
    return computer_choice


def play_game(user_choice, computer_choice):
    try:
        print("OK Now Playing The Game!!")

        if user_choice == computer_choice:
            print("You win")
        else:
            print("Computer win")
    except:
        print("Error playing the game")
