count=0
total=0
range_size=int(input("How many numbers do you have: "))
for i in range(range_size):
  number=float(input("Enter number: "))
  total+=number
  count+=1
avarage=total/count
print(f"the avarage is: {avarage} ")