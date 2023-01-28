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

game_images = [rock, paper, scissors]

user_answer = int((input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")))

if user_answer >= 3 or user_answer <0:
  print("You entered an incorrect answer, you lose")
else:

  print(game_images[user_answer])

  computer_answer = random.randint(0, 2)
  print("Computer chose:")
  print(game_images[computer_answer])

  
  if user_answer == 0 and computer_answer ==2:
    print("You win!")
  elif computer_answer == 0 and user_answer ==2:
    print("You lose")  
  elif computer_answer > user_answer:
    print("You lose")
  elif user_answer > computer_answer:
    print("You win")  
  elif computer_answer == user_answer:
    print("It is a draw")  
  elif user_answer >= 3 or user_answer <0:
    print("You entered an incorrect answer, you lose")   


#if computer_answer == 0:
 # print(rock)
#if computer_answer == 1:
 # print(paper)
#else:
 # print(scissors)    
#print(f"Computer chose {computer_answer}")



  