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
import sys

Choose = int(input("What do you choose? Type 0 form Rock, 1 for Paper or 2 for Scissors.\n"))
# 
# printtype(Choose)
print("You Choose\n")
if Choose == 0:
  print(rock)

elif Choose == 1:
  print(paper)

elif Choose == 2:
  print(scissors)

else:
  print("Wrong Input.. You Lost.!!!")
  sys.exit()
     
print("Computer Choose\n")
Computer_Choose = random.randint(0,2)

if Computer_Choose == 0:
  print(rock)

elif Computer_Choose == 1:
  print(paper)

else:
  print(scissors)


if Choose == 0 and Computer_Choose == 1:
  print("You Lost")
elif Choose == 0 and Computer_Choose == 2:
  print("You Won")
elif Choose == 1 and Computer_Choose == 0:
  print("You Won")
elif Choose == 1 and Computer_Choose == 2:
  print("You Lost")
elif Choose == 2 and Computer_Choose == 0:
  print("You Lost")
elif Choose == 2 and Computer_Choose == 1:
  print("You Won")
elif Choose == Computer_Choose:
  print("Try Again")
elif Choose == Computer_Choose:
  print("Lost")
