#--------Number Guessing Game--------
import random
from day12LOGO import logo
number= random.randint(1,100)
# should_continue= True
def guess():
    # global should_continue
    guess = int(input("Make a guess: "))
    if guess<number:
        print("Too low.\nGuess again.")
        return False
    elif guess>number:
        print("Too high.\nGuess again.")
        return False
    else:
        print("You Win.")
        return True
        # should_continue=False               ##modifying global variable is not an efficient way in programming instead you can return 

def level(attempts):
    # global should_continue
    while attempts>0 :##and should_continue:
            print(f"You have {attempts} attempts remaining to guess the number.")
            if guess():
                return
            attempts-=1
    # if attempts==0 and should_continue:
    print(f"You've run out of attempts. You loose.")
        # should_continue=False

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
    print(number)

    if difficulty=='easy':
        level(10)     
    elif difficulty=='hard':
        level(5) 
    else:
        print("Invalid Input.")

play_game()