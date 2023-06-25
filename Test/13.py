import random as rd

def rock_paper_scissors(choce,options):
    pick = rd.choice(options)
    if choce == pick:
        print(f"User Won\nComputer also choosed {pick}" )
    else:
        print(f"Computer Won\nComputer choosed {pick}")


options=['Rock', 'Paper', 'Scissors']
key = input("Enter your choice: ")
rock_paper_scissors(key,options)