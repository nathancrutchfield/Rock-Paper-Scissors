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

#Write your code below this line 👇
import random
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())
computer_choice = random.randint(0,2)
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)
else:
    print("Invalid choice")

print("Computer chose:")
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)

if user_choice == computer_choice:
  print("Draw")

if user_choice == 0:
  if computer_choice == 1:
    print("You lose")
  elif computer_choice == 2:
    print("You win")

if user_choice == 1:
  if computer_choice == 0:
    print("You win")
  elif computer_choice == 2:
    print("You lose")

if user_choice == 2:
  if computer_choice == 0:
    print("You lose")
  elif computer_choice == 1:
    print("You win")
    