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

#Write your code below this line 👇
game_iamge =[rock,paper,scissors]
user_Choice = int(input("What do you choose? Type 0 form Rock, 1 for Paper or 2 for Scissors.\n"))
if user_Choice >=3 or user_Choice < 0:
  print("You typed an invilid number, you lose!")
else:
  print(game_iamge[user_Choice])
  
  
  computer_Choice = random.randint(0,2)
  print(f"Computer chose{computer_Choice}")
  print(game_iamge[computer_Choice])
  
  
  
  if user_Choice == 0 and computer_Choice == 2:
    print("You win!")
  elif computer_Choice == 0 and  user_Choice== 2:
    print("You lost!")
  elif computer_Choice > user_Choice :
    print("You lose")
  elif user_Choice > computer_Choice :
    print("You Win!")
  elif computer_Choice == user_Choice:
    print("It's a draw")

