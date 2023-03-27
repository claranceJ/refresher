# while loop
while True:
  try:
    # user inputs number
    x=int(input("Enter a number: "))
  except ValueError:
    print("Invalid input, Enter a number")
    continue
  # conditions to check what the user has entered
  if  x%3==0 and x%5==0:
      print(f"{x} is a multiple of both 3 and 5")
  elif x%3==0:
      print(f"{x} is a multiple of 3")
  elif x%5==0:
      print(f"{x} is a multiple of 5") 
  else:
      print(f"{x} is not a multiple of either 3 or 5")
    
