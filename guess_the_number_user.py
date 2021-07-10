import random

def computer_guess(x):
    low = 1
    high = x
    feedback= ' ' #initilizing to an empty string
    while feedback != 'c':
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low #could also be high b/c low = high    
            feedback =input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower() #turns input srting into lower case
            if feedback == 'h':
                high = guess - 1 #if the comp guesses eight but that's too high then we need to adjust our upper bound limit by subtracting one from the incorrect high guess 
            elif feedback == 'l':
                low = guess +1

    print(f"Cool! The computer guessed your number, {guess} correctly")                

computer_guess(10)


