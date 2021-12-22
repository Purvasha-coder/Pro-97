import random
number=random.randint(1,9)
print("Welcome to Number Guessing Game")
chances=0
print("Note for the user-Please enter numbers from 1-9")
while chances<5:
    Usersguessedno=int(input("Enter your Number please"))
    if Usersguessedno==number:
        print("You guessed it right")
        break
    elif Usersguessedno<number:
        print("The guess was too low.Guess a higher number.")
    else:
        print("The guess was too high.Guess a lower number.")
    chances=chances+1
if not chances<5:
    print("You lost!")