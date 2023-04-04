enter=input("Enter word: ")

words=enter.split()
counts=dict()

for word in words:
  counts[word]=counts.get(word, 0) + 1

print(counts)
