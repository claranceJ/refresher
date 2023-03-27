# importing  random library
import random

# user name
name=input("Enter your name: ")
print(f"Welcome {name} to the rock, paper,scissors game ")
# iteration using the while loop
while True:
  # assigning the random function a variable
  computer = random.randrange(0,3)
  # assigning the rock paper and scissors to the computer
  if computer==0:
    comp="rock"
  elif computer==1:
    comp="scissors"
  elif computer ==2:
    comp="paper"
  # options of the game
  print("Enter rock,paper or scissors")
  
  # user to input as a player
  player=input("Enter your choice: ")

  # making sure the user enters the right choice
  if player.lower() not in["rock","paper","scissors"]:
    print("Invalid input!")
    continue

    #print what the computer chooses randomly 
  print(f"The computer chooses {comp}")

  # comparing between the player choice and computer choice
  
  # comaparing 0 which is rock for the computer
  if computer == 0 and("Rock" in player or "rock" in player):
    print("rock and rock, its a draw!")
  elif computer == 0 and ("Scissors" in player or "scissors" in player):
    print("rock smashes scissors, Computer wins!")
  elif computer == 0 and ("Paper" in player or "paper" in player):
    print(f"paper covers rock, {name} wins")
  # comaparing 1 which is scissors for the computer
  if computer == 1 and("Rock" in player or "rock" in player):
    print(f"rock smashes scissors, {name} wins!")
  elif computer == 1 and ("Scissors" in player or "scissors" in player):
    print("scissors and scissors, its a draw!")
  elif computer == 1 and ("Paper" in player or "paper" in player):
    print("scissors cuts paper, computer wins")

  # comaparing 2 which is paper for the computer
  if computer == 2 and("Rock" in player or "rock" in player):
    print("paper covers rock, computer wins!")
  elif computer == 2 and ("Scissors" in player or "scissors" in player):
    print(f"scissors cuts paper, {name} wins!")
  elif computer == 2 and ("Paper" in player or "paper" in player):
    print("paper and paper, its a draw!")