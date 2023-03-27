# print 1 to 100
# note the multiples of 3 and 5


for i in range(1,101):
  if i%3==0:
    print(f"{i} is a multiple of 3")
  elif i%5==0:
      print(f"{i} is a multiple of 5")
  else:
    print(i)