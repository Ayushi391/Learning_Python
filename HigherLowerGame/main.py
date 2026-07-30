#HIGHER LOWER GAME
import random, os
from art import logo, logo2
from game_data import data
print(logo)

def clear():
    if os.name == "nt":      # Windows
        os.system("cls")
    else:                    # macOS and Linux
        os.system("clear")

def compare(A,B):
    User_ans =input("Who has more followers? Type 'A' or 'B': ").lower()
    if (
        A["follower_count"]>B["follower_count"] and User_ans=='a'      # 'and' has higher precidence than 'or'.
        ) or (
        B["follower_count"]>A["follower_count"] and User_ans=='b'):
        return True 
    elif (
        A["follower_count"]>B["follower_count"] and User_ans=='b' 
        ) or (
        B["follower_count"]>A["follower_count"] and User_ans=='a'):
        return False
    else:
        print("Invalid Input.")
        return False

def get_random_person(exclude):
    '''Returns a random person different from excluded one.'''
    person=random.choice(data)
    while person==exclude:
        person =random.choice(data)
    return person

random_A = random.choice(data)
random_B = get_random_person(random_A)
score=0
should_continue = True
while should_continue:
    print(f"Compare A: {random_A["name"]}, a {random_A["description"]}, from {random_A["country"]}.")
    print(logo2)
    print(f"Against B: {random_B["name"]}, a {random_B["description"]}, from {random_B["country"]}.")
    correct=compare(random_A,random_B)
    if correct:
        clear()
        print(logo)
        score+=1
        print(f"You're right! Current score:{score}")
        random_A=random_B
        random_B=get_random_person(random_A)
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break