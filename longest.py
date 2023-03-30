# Find the longest word in the user input

# Initial empty list
list=[]
# prompt the user 5 times
for i in range(5):
  # get list of words from user
  words=input("Enter a word: ")
  # append on a list
  list.append(words)

longest=list[0]
# loop through to find the longest word in the list
for long in list:
  if len(long)>len(longest):
    longest=long
print(longest)


