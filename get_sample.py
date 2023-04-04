counts=dict()

languages=["python","php","python","c+","java","php","javascript","javascript"]

for language in languages:
  counts[language]=counts.get(language, 0)+1

print(counts)