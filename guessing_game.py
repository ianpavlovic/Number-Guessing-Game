import random
import sys

SOLUTION = random.randint(1,10)

def intro():
    print("--------------------------------------")
    print("Hello, Welcome to Number Guessing Game")
    print("--------------------------------------\n")

def game():
    try:
        tries = 1
        number_chosen = int(input("Please pick a number form 1 to 10  "))
    except ValueError:
        print("Thats not a valid value please try again...")
    else:
        while number_chosen != SOLUTION:
            if number_chosen < SOLUTION:
                print("It's Higher")
                tries += 1
                number_chosen = int(input("Please pick a number form 1 to 10  "))
            elif number_chosen > SOLUTION:
                print("It's Lower")
                tries += 1
                number_chosen = int(input("Please pick a number form 1 to 10  "))
        print("You got it! YOU WON!!")
        print("You got it in a total of {} tries".format(tries))
        play_again()

def play_again():
    next_game = input("Would you like to play again?? [y]es / [n]o:  ").lower()
    if next_game == "n":
        print("Thank you for playing. See you next time =)")
        sys.exit(0)
    elif next_game == "y":
        play_game()

def play_game():
    intro()
    game()

play_game()
