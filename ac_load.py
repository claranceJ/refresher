# input from user
width=int(input("Enter width: "))
height=int(input("Enter height: "))
number_of_people=int(input("Enter number of people: "))
# calculate horse power
horsepower=width*height*0.1+number_of_people*0.06
# print horsepower
print(f"{horsepower:.2f}")