while True:
  try:
     # asking user how many books they want to buy
    books=int(input("How many books do you want to buy?: "))
    # asking user how much they have
    money=int(input("How much money do you have?: "))
    # calculate the total required and compare with what the user has 
  except ValueError:
    print("Invalid Input, Enter the correct input")
    continue
  total_cost=books*20
  # the difference in the amount required
  difference=total_cost-money
  if money>=total_cost:
    print("You have enough money, go for it!")
  elif money<total_cost:
    print(f"You need ${difference} more to buy that number of books")
    