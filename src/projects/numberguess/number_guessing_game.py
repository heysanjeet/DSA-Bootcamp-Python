import  random

number_to_guess=random.randint(1, 100)
while True:
 try:
  guess=int(input("Enter a number between 1 to 100: "))
  if guess> number_to_guess:
      print("To High!")
  elif guess< number_to_guess:
      print("To Low!")
  else:
    print("Configuration, you guessed the number!")
    break
 except ValueError:
  print("Please Enter a valid number")