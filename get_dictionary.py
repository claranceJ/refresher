cars=dict()
names=["urus","lexus","mark-x","mazda","urus","mobius","urus","lexus","mazda","urus"]

for name in names:
  cars[name]=cars.get(name, 0)+1

print(cars)