found=False
print(found)

for number in [8,9,54,89,67,3,56]:
  if number==3:
    found=True
    print(number, found)
    break
  elif number!=3:
    print(number, found)
   