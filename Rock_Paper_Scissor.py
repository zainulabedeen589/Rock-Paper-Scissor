"""
 WORKFLOW OF PROJECT :
 1- Input from user(rock, paper, scissor)
 2- Computer choise (Computer will choos randomly not conditionally)


Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B = Paper
Paper - Paper = tie
Paper - Rock = Paper
Paper - Scissor = Scissor

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""

import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both choice same: Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer win")
    else :
        print("Rock smashes Scissor = You win")
        
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper = Computer win")
    else :
        print("Paper covers Rock = You win")
        
elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes Scissor = Computer win")
    else :
        print("Scissor cuts Paper = You win")        