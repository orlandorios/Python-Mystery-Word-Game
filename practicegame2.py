# import the random module
import random

#choose words or import text file for words that will be used and selected at random
def choose_word():
    words = ["Cena", "Orton", "Woods", "Kingston", "Lesnar", "Reigns"]
    word = random.choice(words).lower()
    return word

def word_in_progress(word, guesses):
    #takes 2 parameters
    word_in_progress = ""
    #start with an empty and build up to current state with correct guesses
    for letter in word:
        if letter in guesses:
            word_in_progress += letter
        else:
            word_in_progress += "*"
    return word_in_progress
#for loop will cycle through characters and see if there is correct guess, if not, will leave an astrix

# the main function that handles the game logic and guessing
def main(word):
    lettersguessed = []
    chances = int(len(word) * 2)
    # to make sure the amount guesses is a whole number, make it an integer
    print("You are looking for a word that is " + str(len(word)) + " letters long." )
    
    while True:
        if chances != 0:
            print("\nyou have " + str(chances) + " chances left.")
            print("word so far: " + word_in_progress(word, lettersguessed))
            #This will notify player which state the current word is in
            print("letters guessed: " + str(lettersguessed))
            guess = input("Guess: ").lower()[0]
            
            if word_in_progress(word, lettersguessed) == word:
                print("\nCongratulations! You got the right word: " + word)
                break
            
            else:
                chances -= 1
                if guess in word:
                    print("Correct letter!")
                else:
                    print(guess + " is not in the word.") 

            if guess not in lettersguessed:
                lettersguessed.append(guess)
        else:
            print("\nOops you ran out of guesses. The correct word was " + word)
            #whenever player inputs guess, appending will let user know letters it has used
            break

while True:
    word = choose_word()
    main(word)
    if input("Would you like to continue: y/n ").lower().startswith("n"):
        break
        