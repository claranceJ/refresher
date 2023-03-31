largest=None
print("before", largest)
for value in[23,12,45,90,54,87,20,76,3,10,56,]:
  if largest is None:
    largest=value
  elif value>largest:
    largest=value
  print(value, largest)  
print("after", largest)