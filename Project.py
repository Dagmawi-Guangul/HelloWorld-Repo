#First Code Draft for Hangman
import random
def hangman():
    word = random.choice(["Trash", "Study", "Trunk", "Queen"])
    print("HANGMAN")
    guess = input("Guess a 5 letter word: ")
    if guess == word:
        print("You survived!")
    else:
        print("You lost!")
hangman()









