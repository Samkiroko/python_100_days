    if guess_letter not in random_word:
        lives -= 1
        if lives == 0:
            game_over == True
            print("You lose!!")