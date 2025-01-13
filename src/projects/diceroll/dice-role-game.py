#run the code
import random
from unittest.mock import right

while True:
  choice =input("Do you want to play the game (Y/N): ").lower()
  if choice=='y':
    dice1 =random.randint(1,6)
    dice2= random.randint(1,6)
    print(f"{dice1}, {dice2}")
  elif choice=='n':
    print("Thanks for playing.!")
    break
  else:
    print("invalid choice")

