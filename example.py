import random
import re
master = open("/usr/share/dict/words")
dictionary = master.read()
dictionary = dictionary.lower().split()
def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    easy_word_list = []
    for word in word_list:
        if len(word) >= 4 and len(word) <= 6:
            easy_word_list.append(word)
    return easy_word_list
def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    medium_word_list = []
    for word in word_list:
        if len(word) >= 6 and len(word) <= 8:
            medium_word_list.append(word)
    return medium_word_list
def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    hard_word_list = []
    for word in word_list:
        if len(word) >= 8:
            hard_word_list.append(word)
    return hard_word_list
def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    correct_word = random.choice(word_list)
    return correct_word
def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.
    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.
    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    progress_display = []
    for letter in word:
        if letter in guesses:
            progress_display.append(letter)
        else:
            progress_display.append('_')
    progress_display = ' '.join(progress_display)
    progress_display = progress_display.upper()
    return progress_display
def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    progress = display_word(word, guesses)
    if '_' in progress:
        return False
    else:
        return True


def get_level():
    level = input("What difficulty setting do you want?\n")
    level = input("What difficulty setting do you want? Please enter easy, medium or hard.\n")
    level = level.lower()
    if level == 'easy':
        answer = random_word(easy_words(dictionary))
def gameplay_loop(answer):
            print("You already guessed that!")
        guesses.append(this_guess)
        print(display_word(answer, guesses))
        print("You have {} incorrect guesses left.\n".format(8 - fails))
        print("These are your guesses so far: {}".format(guesses))
        print("You have {} guesses left.\n".format(8 - fails))
        if fails >= 8:
            break
    if fails >= 8:
        play_again_lose = input(("You lose! The word was {}. If you want to play again, enter yes.\n".format(answer)))
        play_again_lose.lower()
        if play_again_lose == 'yes':
            return main()
        else:
            print("Okay, have a nice day!")
    else:
        play_again_win = input(("You won! If you want to play again, enter yes.\n"))
        play_again_win.lower()
        if play_again_win == 'yes':
            return main()
        else:
            print("Okay, have a nice day!")
def main():
    """
    Runs when the program is called from the command-line.
    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level