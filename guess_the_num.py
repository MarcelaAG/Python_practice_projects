import random

def guess(x ):
    random_number = random.randint(1, x) #returns a random integer between 1 and x
    guess = 0 #random.randint will never be 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, but that guess is too low!")
        elif guess > random_number:
            print("Sorry, but that guess is too high!")
    
    print(f"Wow! Good job, you guessed the number {random_number} correctly!")


