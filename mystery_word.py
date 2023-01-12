#Project description: interactive text-based single player word guessing game
#Create function to access text files
#Convert text file words to dictionary or list
#Import random module to choose from list of words

import random

#create function for game word list
#create variable to open file & convert to list
#use random method to randomize word selection
def word_list():
    words = open("words.txt").readlines()
#readlines() method returns list containing each line in the file as a list item
    word = random.choice(words).lower()
    return word
#import random/random.choice tells program to pick random word from a list

def secret_word():
    words = open("secretword.txt").readlines()
    return words

#create function to for player guess
#set 2 parameters, one for the word and another to create blank space for the guess
# guess_word function will be called to loop
def guess_word(word, guesses):
    guess_word = ""
    # start out guess word as empty string and allow to iterate through characters in word
    for character in word:
        if character in guesses:
            guess_word += character
        #create if statement, if character is found in guesses through iteration, add character to word
            
        else:
        #create else statement, if character is not found through iteration, underscore added in its place
            guess_word += " _ "
                
    return guess_word

# create function to set guess limits, correct & wrong answers
# parameter will be what is called for each turn
# use while true loop to have the game repeat for each turn until loop is informed to stop (using break)
# use if/else statements to arrange how many guesses are removed from limit
# use if/else statements to 
# print out/concatenate prompts to display what has occurred after each turn
# print out/concatenate prompts to display characters already used
# print out/concatenate prompt to introduce the game

def game_function(word):
    character_guess = []
    #create starting empty list for characters guessed to append with player input
    guess_limit = 8
    print("\n💯 Welcome to Orlando's " + '"Guess-it Game!"' + " Let's get it poppin! 💯")
    print("\nThis word contains " + str(len(word)) + " letters")
    # print game introduction before while loop, so it does not keep looping during
    
    
    while True:
        if guess_limit != 0:
        # use is not equal function (!=) to notify if guess_limit not at 0, still about to guess/loop continues
            print("\nYou got " + str(guess_limit) + " more guesses left in the bag")
            print("\nWord is: " + guess_word(word, character_guess))
            # used print and call guess_word function to show current state of word and character guess
            print("Letters guessed: " + "" + str(character_guess))
                
            if guess_word(word, character_guess) == word:
                print("\nNailed it! " + 'The word "' + word + '" is the correct answer! 🔥🔥🔥')
                break
            guess = input("Guessed: ").lower()[0]
            
            if guess in character_guess:
                guess_limit == 0
                print("\nYou've already used that letter! Rewind that back, bruh!")
                
            # create if statement if guess is already included in character guess list
            # if guessed input is already in list, used equality operator for keep guess limit true in current state
            
            else:
                guess_limit -= 1
                if guess in word:
                    print("\nHA! Got'emmm! " + "letter " + "'" + guess + "'" + " is correct!")
                    
                else:
                    print("\nNah fam, the letter " + '"' + guess + '"' + " ain't it!")
            
                    
            if guess not in character_guess:
                character_guess.append(guess)
                # append character_guess with guess variable input. This will add input letters in to character guess list
                # created if/else not statement to only include input not already currently in list
        else: 
            print("\nYou ran out of guesses! The correct word is " + word)
            break
        # else statement to break loop/end game if guess limit reaches 0

# Create while loop outside main function to allow loop to be ended
while True:
    word = word_list()
    game_function(word)
    if input("Run it back? y/n/!: ").lower().startswith("n"):
        if input().lower().startswith("!"):
            secret = secret_word()
            game_function(secret)
    break
    
# def play_game():
#     pass




# if __name__ == "__main__":
#     # play_game()
