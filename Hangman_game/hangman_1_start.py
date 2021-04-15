# Step 1
import random
from replit import clear
from hangman_words import word_list
from hangman_art import stages, logo


random_word = random.choice(word_list).lower()
word_length = len(random_word)
game_over = False
lives = 6

# DONE-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

print(logo)
# Test code
print(f"psst, the solution is {random_word}")

display = []
for _ in range(word_length):
    display += "_"

while not game_over:
    # -2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess_letter = (input("Guess letter in the secret word?\n")).lower()

    clear()

    if guess_letter in display:
        print(f"You've already guessed {guess_letter}")

    for position in range(word_length):
        letter = random_word[position]
        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess_letter}")
        if letter == guess_letter:
            display[position] = letter

    if guess_letter not in random_word:
        print(
            f"You guessed {guess_letter}, that's not in the word.You lose a life")
        lives -= 1
        if lives == 0:
            print("You lose!!")
            game_over = True
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("you win!!")

    print(stages[lives])
