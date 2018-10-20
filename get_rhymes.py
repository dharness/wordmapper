import sys
from collections import defaultdict
import requests
import argparse

def main(args):
  with open(f'./by_letter/{args.letter}.csv', 'r') as infile:
    words = infile.read().split('\n')
    rhymes_by_word = defaultdict(set)

    for i, word in enumerate(words):
      word = word.lower()
      sys.stdout.write(f'Fetching: {str(i/len(words))} %\r')
      sys.stdout.flush()
      r = requests.get(f'https://api.datamuse.com/words?rel_rhy={word}')

      rhymes = set()
      for rhyme_data in r.json():
        rhyme = rhyme_data['word']
        if ' ' not in rhyme:
          rhymes.add(rhyme.lower())

      rhymes_by_word[word] = rhymes
  print('Fetching complete. Processing...')  
  write_to_csv(rhymes_by_word, args.letter)
  print('Writing complete.')  


def write_to_csv(rhymes_by_word, letter):
  with open(f'./rhymes_by_letter/{letter}.csv', 'w') as outfile:
    for word, rhymes in rhymes_by_word.items():
      sys.stdout.write(f'Writing: {len(rhymes_by_word)} %\r')
      sys.stdout.flush()
      outfile.write(f"{word},{','.join(list(rhymes))}\n")


parser = argparse.ArgumentParser()
parser.add_argument('--letter', type=str)

args = parser.parse_args()
main(args)