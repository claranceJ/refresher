cars=dict()
names=["urus","lexus","mark-x","mazda","urus","mobius","urus","lexus","mazda","urus"]

for name in names:
  if name not in cars:
    cars[name]=1
  else:
    cars[name]=cars[name]+1
print(cars) 