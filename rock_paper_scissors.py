import random

def play():
    user= input("Make your choice, 'r' for rock, 'p' for paper or 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer :
        return "It's a tie!"

    #r>s, s>p, p>r (these are our rules)
    if is_win(user, computer):
        return "You are the winner!"
    #this doesn't need an if statement 
    return "Bummer, you lost!"

#this is our helper function
def is_win(player, opponent):
    #we are going to return true if player wins
    #r>s, s>p, p>r (these are our rules)
    if (player == 'r' and opponent =='s') or (player == 's' and opponent =='p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())