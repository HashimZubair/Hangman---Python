# This is a hangman game
import random

# Picks a random word from the file of words
def get_random_word():
    with open("hangman_words.txt", "r") as file:
        lines = file.read().splitlines()
        word = random.choice(lines)
    file.close()
    return word

# Converts the chosen word into stars to display to the player
def word_to_star(word_to_star):
    star_word = ""
    for letter in word_to_star:
        if letter != "\n":
            star_word += "*"
    return star_word

def hangman_dead():
    print(" __________")
    print(" |       | |")
    print("\O/      | |")
    print(" |       | |")
    print("/ \   ----------")
    print("      | |    | |")
    return ""

def hangman_loop():
    num_tries = 0
    max_tries = 6  # head, body, 2 arms, 2 legs (total 6 tries)
    tries_left = 6
    hangman_word = get_random_word()
    hangman_word_star = list(word_to_star(hangman_word))

    while True:
        if num_tries == max_tries:
            print(hangman_dead())
            print("You lost. The word was '" + hangman_word + "'.")
            break

        if "".join(hangman_word_star) == hangman_word:
            print("You won! The word was '" + hangman_word +"'.")
            break

        print("\nWord to guess: " + "".join(hangman_word_star))
        guess = input("Enter a word or letter: ")

        if guess in hangman_word:
            if 1 < len(guess) < len(hangman_word):
                print("Please enter a letter or a full word!")
            elif guess == hangman_word:
                print("\nYou won! The word was '" + hangman_word + "'.")
                break
            else:
                print("\nNice! The letter/word '" + guess + "' is in the word!")
                print("You still have " + str(tries_left) + " tries remaining.")
                for x in range(len(hangman_word)):
                    if hangman_word[x] == guess:
                        hangman_word_star[x] = guess

        else:
            print("\nThe letter/word '" + guess + "' is not in the word!")
            tries_left -= 1
            num_tries += 1
            print("You have " + str(tries_left) + " tries remaining!")

    return "Game Ended."

print("Welcome to Hangman! Category: Animal Names")
print("You get 6 tries to guess the correct word.")

print(hangman_loop())



