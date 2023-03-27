while True:
  # user input
  password = input("password: ")
  # length of password
  if len(password) > 8:
    # number in password
    if any(number in password for number in "0123456789"):
      # lowercase in password
      if password != password.lower():
        # uppercase in password
        if password != password.upper():
          print("Password valid. Account created.") 
        else:
          print("password must contain a lowercase letter")
      else:
        print("password must contain an uppercase letter")
    else:
      print("password must contain a number")
  else:
    print("password too short, must be more than 8 characters.")
