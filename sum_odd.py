# find total of odd numbers in the list
numbers = [
    62, 60, 53, 53, 33, 3, 25, 61, 36, 1, 69, 55, 56, 39, 32, 76, 20, 62, 47
]

# set an initial value
sum=0
# loop to find the odd numbers
for number in numbers:
  if number%2!=0:
    # add the odd numbers
    # update the initial value
    sum+=number
# print the total    
print(sum)


