# Rock Paper Scissors Game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to Rock Paper Scissors Game ")

choose = [rock, paper, scissors]
name = input("Your nice name?")


play_input = int(input("Choose 0=Rock, 1=Paper & 2=Scissors?\n"))
try:
    play_result = choose[play_input]
    print(play_result)

    computer_play = random.randint(0, 2)
    computer_result = choose[computer_play]
    print(computer_result)

    # check wins or draw

    if play_result == computer_result:
        print("Its a draw")
    elif play_result == rock and computer_result == scissors:
        print(f"{name} wins")
    elif computer_result == rock and play_result == scissors:
        print("Computer wins")
    elif play_result == scissors and computer_result == paper:
        print(f"{name} wins")
    elif computer_result == scissors and play_result == paper:
        print("Computer wins")
    elif play_result == paper and computer_result == rock:
        print(f"{name} wins")
    elif computer_result == paper and play_result == rock:
        print("Computer wins")
    elif play_input >= 3 or computer_result >= 3:
        print("Wrong input!! please try again😎")
    else:
        print("Wrong input please try again")
except:
    print("Wrong input please try again")
