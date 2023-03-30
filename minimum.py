# write a program that finds the minimum value that the user enters

while True:
  # get the user input
  user=int(input("How many numbers will you enter?: "))
  # set initial value
  minimum=[]
  # go through the input
  for i in range(user):
    number=int(input("Enter a number: "))
    minimum.append(number)
  lowest=minimum[0]
  # find the minimum value
  for mini in minimum:
    if mini<lowest:
      lowest=mini
  print(f"the lowest number is {lowest}")
      
  
  

