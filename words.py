count=dict()
enter=input("Enter words to count: ")
words=enter.split()

print(words)
for word in words:
  count[word]=count.get(word, 0)+1

print("Counting.....")

print("Count is", count)