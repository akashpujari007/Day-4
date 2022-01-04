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

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if choose == 0:
  print(rock)
elif choose == 1:
  print(paper)
elif choose == 2:
  print(scissors)

print("Computer choose:\n")

import random

game_list = [rock, paper, scissors]
Computer_choice = random.choice(game_list)
print(Computer_choice)

if choose >= 3 or choose < 0:
  print("Invalid number")
elif choose == 0 and Computer_choice == rock:
  print("Draw")
elif choose == 1 and Computer_choice == paper:
  print("Draw")
elif choose == 2 and Computer_choice == scissors:
  print("Draw")
elif choose == 0 and Computer_choice == scissors:
  print("You Won")
elif choose == 0 and Computer_choice == paper:
  print("You Lose")
elif choose == 1 and Computer_choice == rock:
  print("You Won")
elif choose == 1 and Computer_choice == scissors:
  print("You Lose")
elif choose == 2 and Computer_choice == rock:
  print("You Lose")
elif choose == 2 and Computer_choice == paper:
  print("You Won")

