numb_list=list()
range_numb=int(input("How many numbers do you have?: "))

for i in range(range_numb):
  numbers=int(input("Enter number: "))
  numb_list.append(numbers)

print("the avarage is: ",sum(numb_list)/len(numb_list))
  