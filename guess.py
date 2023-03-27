# import random
import random

print("I'm thinking of a number between 1 and 99")



secret_num=random.randint(1,99)

# Iterrate through the conditions
while True:
  # warning invalid input
  try:
    guess=int(input("Enter a guess: "))
  except ValueError:
    print("Invalid input!")
    continue
  # condition to check the number
  if guess>secret_num:
    print("Your guess is too high")
  elif guess<secret_num:
    print("Your guess is too low!")
  elif guess==secret_num:
    print(f"Congrats! the number was {secret_num}")