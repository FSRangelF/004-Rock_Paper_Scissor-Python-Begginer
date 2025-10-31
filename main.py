import random

rock = r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
cpu_choice = int(random.randint(0, 2))

if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print("\nYou typed an invalid option")

print("\nComputer chose:\n")

if cpu_choice == 0:
    print(rock)
elif cpu_choice == 1:
    print(paper)
else:
    print(scissors)

if player_choice == cpu_choice:
    print("\nDraw")
elif player_choice == 0 and cpu_choice == 2:
    print("\nYou Won!")
elif player_choice == 1 and cpu_choice == 0:
    print("\nYou Won!")
elif player_choice == 2 and cpu_choice == 1:
    print("\nYou Won!")
else:
    print("\nYou lose!")
    