
while True:
  # ask user for input
  weight=int(input("Enter your weight in kg: "))
  height=float(input('Enter your height in meters: '))
  # bmi formular
  bmi=weight/(height*height)
  # checking where the user falls under
  if bmi <18.5:
    print(f"Your bmi is {bmi:.3f}.You are Underweght")
  elif bmi> 18.5 and bmi<24.9:
    print(f"Your bmi is {bmi:.3f}.You have a normal weight")
  elif bmi>25 and bmi<29.9:
    print(f"Your bmi is {bmi:.3f}.You are Overweight")
  else:
    print(f"Your bmi is {bmi:.3f}.You are Obess")
    # checking if the user wants to continue
  user=input("Do you want to continue?:(yes/no) ")
  if user.lower()=="n":
    break