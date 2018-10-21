import sys
from collections import defaultdict
import argparse
import json

import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)


async def main(args):
    async with aiohttp.ClientSession() as session:
        with open(f'./chunks/{args.chunk_name}.csv', 'r') as infile:
            words = infile.read().split('\n')
            words = words
            rhymes_by_word = defaultdict(set)

            for i, word in enumerate(words):
                word = word.lower()
                sys.stdout.write(f'Fetching: {str(i/len(words))} %\r')
                sys.stdout.flush()
                r = await fetch(session, f'https://api.datamuse.com/words?rel_rhy={word}')
                results = json.loads(r)
                rhymes = set()
                for rhyme_data in results:
                    rhyme = rhyme_data['word']
                    if ' ' not in rhyme:
                        rhymes.add(rhyme.lower())

                rhymes_by_word[word] = rhymes

    print('Fetching complete. Processing...')  
    write_to_csv(rhymes_by_word, args.chunk_name)
    print('Writing complete.')  


def write_to_csv(rhymes_by_word, chunk_name):
  with open(f'./rhymes_by_chunk/{chunk_name}.csv', 'w') as outfile:
    for word, rhymes in rhymes_by_word.items():
      sys.stdout.write(f'Writing: {len(rhymes_by_word)} %\r')
      sys.stdout.flush()
      outfile.write(f"{word},{','.join(list(rhymes))}\n")


parser = argparse.ArgumentParser()
parser.add_argument('--chunk_name', type=str)

args = parser.parse_args()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(args))