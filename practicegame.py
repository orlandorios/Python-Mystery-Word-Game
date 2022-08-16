#Project description: interactive text-based single player word guessing game
#Create function to access text files
#Convert text file words to dictionary or list
#Import random module to choose from list of words

import random

#create function for game word list
#create variable to open file & convert to list
#use random method to randomize word selection
def word_list():
    # words = ['pizza' , 'cheese' , 'raccoon' , 'daddy', 'chester']
    words = open("test-word.txt").readlines()
#readlines() method returns list containing each line in the file as a list item
    word = random.choice(words).lower()
    return word
#import random/random.choice tells program to pick random word from a list

#create function to for player guess
#set parameters to include word & 
def guess_word(word, guesses):
    guess_word = ""
    for character in word:
        if character in guesses:
            guess_word += character
            
        else: 
            guess_word += " _ "
                
    return guess_word

def game_function(word):
    letter_guess = []
    guess_limit = 8
    print("\n💯 Welcome to Orlando's " + '"Guess-it Game!"' + " Let's get it poppin! 💯")
    print("\nThis word contains " + str(len(word)) + " letters")
    
    while True:
        if guess_limit != 0:
            print("\nYou got " + str(guess_limit) + " more guesses left in the bag")
            print("\nWord is : " + guess_word(word, letter_guess))
            print("Letters guessed : " + str(letter_guess))
            guessing = input("Guessed: ").lower()[0]
                
            if guess_word(word, letter_guess) == word:
                print("\nNailed it! " + 'The word "' + word + '" is the correct answer! 🔥🔥🔥')
                break
            
            if guessing in letter_guess:
                guess_limit == 0
                print("You've already used that letter! Rewind that back, bruh!")       
            
            else:
                guess_limit -= 1
                if guessing in word:
                    print("\nHA! Got'emmm! " + "letter " + "'" + guessing + "'" + " is correct!")
                    
                else:
                    print("\nNah fam, the letter " + '"' + guessing + '"' + " ain't it!")
            
                    
            if guessing not in letter_guess:
                letter_guess.append(guessing)        
                
        else: 
            print("\nYou ran out of guesses! The correct word is " + word)
            break
                
while True:
    word = word_list()
    game_function(word)
    if input("Run it back? y/n: ").lower().startswith("n"):
        break