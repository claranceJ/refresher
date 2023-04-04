name=input("Enter file name: ")
handles=open(name)

counts=dict()

for handle in handles:
  words=handle.split()
  for word in words:
    counts[word]=counts.get(word, 0)+1

print(counts)