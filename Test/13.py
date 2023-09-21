import random as rd

def rock_paper_scissors(choce,options):
    pick = rd.choice(options)
    if choce == 'Rock' and pick == 'Scissor':
        print("User Wins")
    elif choce == pick:
        print("It is a Tie")
    elif choce == 'Scissor' and pick == 'Paper':
        print("User Wins")
    elif choce == 'Paper' and pick == 'Rock':
        print("User Wins")
    else:
        print("Computer Wins")
options=['Rock', 'Paper', 'Scissor']
key = input("Enter your choice: ")
rock_paper_scissors(key,options)
