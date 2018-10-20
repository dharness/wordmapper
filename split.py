from collections import defaultdict
from pprint import pprint

with open('./words.csv', 'r') as f:
  words = f.read().split('\n')
  by_letter = defaultdict(list)
  for word in words:
    word = word.lower()
    if len(word) > 0:
      by_letter[word[0]].append(word)

for letter in by_letter:
  with open(f'./by_letter/{letter}.csv', 'a') as outfile:
    out = '\n'.join(by_letter[letter])
    outfile.write(out)