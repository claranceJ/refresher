total=0
count=0

while True:
  number=(input("Enter number: "))
  if number == "done":
    break
  value=float(number)
  total+=value
  count+=1
avarage=total/count
print(f"The avarage is: {avarage}"