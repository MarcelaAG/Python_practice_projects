import random
from words import words
import string

#we can't use words with dashes or spaces so we create this function
def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something(word) from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
#we need to be able to keep track of which letters were guessed and which letters in the word were correctly guessed
#also need to keep track of what is a valid letter
def hangman():
      word = get_valid_word(words)
      word_letters = set(word)      #this variable saves all the letters in a word as a set , keeps track of what already has been guessed in the word
      alphabet = set(string.ascii_uppercase) #American Standard Code for Information Interchange
      used_letters = set() #will keep track of what the user has guessed
      
      lives = 6

      #this is how we get our user input
      while len(word_letters) > 0 and lives > 0: #we will keep iterating through the below statements until all the letters have been guessedS
            #we need to tell the user which letters have been used
            print("You have: ", lives, "lives remaining and you have used these letters: ", ' '.join(used_letters)) #this turns this iterable into a string seperated by  whatever the string is b/f the .join
            #we also need to tell the used what the current word is but with - and the letters that are correct (i.e W-RD)
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print("Current word: ", ' '.join(word_list))
            user_letter = input("Guess a letter: ").upper()
            if user_letter in alphabet - used_letters: #if this is a valid letter that has not been used yet it will get added to the used letters set
                used_letters.add(user_letter)
                if user_letter in word_letters: #if the letter that was just guessed is in the word then it will get removed from set of word letters
                    word_letters.remove(user_letter)
                else:
                    lives= lives -1    #takes one life away if the letter is not in the word
                    print('The letter you guessed is not in the word.')
            elif user_letter in used_letters:
                print("You have already used that character. You need to try again.")        
            else:
                print("Invalid character, try again!")

        #we get here when len(word_letters) ==0 OR when lives ==0
      if lives ==0:
            print("Oh no! You died. The word was: ", word)
      else:    
            print("You guessed ", word, "correctly!")

hangman()
