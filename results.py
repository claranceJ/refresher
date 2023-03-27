while True:
  try:
    # user input
    score=int(input("What is your score?: "))
  except ValueError:
    print("Invalid, Enter the correct score")
    continue
  # condition for >70, otherwise try again 
  if score>=70:
    print("You passed!")
  else:
    print("Try again")
  
  