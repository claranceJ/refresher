cars=[]

for key, val in counts.items():
  rev=(val,key)
  cars.append(rev)

cars=sorted(cars, reverse=True)

print(cars)