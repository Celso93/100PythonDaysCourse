import random

# jakenpo game

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

draw = [rock,paper,scissors]
your_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
computer_choice = random.randint(0, 2)

if your_choice == computer_choice:
    print(draw[your_choice])
    print(f"Computer chose: {draw[computer_choice]}")
    print("It`s a draw")
elif your_choice == 0 and computer_choice == 1:
    print(draw[your_choice])
    print(f"Computer chose: {draw[computer_choice]}")
    print("You lose!")
elif your_choice == 0 and computer_choice == 2:
    print(draw[your_choice])
    print(f"Computer chose: {draw[computer_choice]}")
    print("You win!")
elif your_choice == 1 and computer_choice == 2:
    print(draw[your_choice])
    print(f"Computer chose: {draw[computer_choice]}")
    print("You lose!")
elif your_choice == 0 and computer_choice == 1:
    print(draw[your_choice])
    print(f"Computer chose: {draw[computer_choice]}")
    print("You lose!")
elif your_choice == 0 and computer_choice == 2:
    print(draw[your_choice])
    print(f"Computer chose: {draw[computer_choice]}")
    print("You win!")
elif your_choice == 1 and computer_choice == 0:
    print(draw[your_choice])
    print(f"Computer chose: {draw[computer_choice]}")
    print("You win!")
else:
    print("Not Valid entered")