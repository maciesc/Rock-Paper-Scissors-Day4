import random
from os import system, name
import time

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


draw = "You draw"
lose = "You lose"
win = "You win"

drawing = {
  0: rock,
  1: paper,
  2: scissors,
}

solutions = { 
  (0,0): draw,
  (0,1): lose,
  (0,2): win,
  (1,0): win,
  (1,1): draw,
  (1,2): lose,
  (2,0): lose,
  (2,1): win,
  (2,2): lose,
}

def clear_console():
   # for windows
   if name == 'nt':
      _ = system('cls')

   # for mac and linux
   else:
     _ = system('clear')
     
while(True):
  print("Welcome to the game rock paper scissors")
  user_choice = input("Type '0' for rock, '1' for paper and 'anything else' for scissors\n")
  if user_choice.isdigit() and 0 <= int(user_choice) <= 2:
    user_choice = int(user_choice)
    
  else:
    user_choice = 2

  computer_choice = random.randint(0, 2)

  print("Your choice\n")
  print(drawing[user_choice])
  
  print("\n")
  print("Computer choice\n")
  print(drawing[computer_choice])

  print(solutions.get((user_choice, computer_choice), "Please type correct value"))
  time.sleep(2)
  clear_console()
  
