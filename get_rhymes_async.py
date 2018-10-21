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
        with open(args.chunk_path, 'r') as infile:
            words = infile.read().split('\n')
            rhymes_by_word = defaultdict(set)

            for i, word in enumerate(words):
                word = word.lower()
                sys.stdout.write(f'Fetching: {str(100*i/len(words))} %\r')
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
    part_name = args.chunk_path.split('/')[-1]
    out_path = f'./rhymes_by_part/{part_name}.csv'
    write_to_csv(rhymes_by_word, out_path)
    print('Writing complete.')  


def write_to_csv(rhymes_by_word, out_path):
    with open(out_path, 'w') as outfile:
        for word, rhymes in rhymes_by_word.items():
            sys.stdout.write(f'Writing: {len(rhymes_by_word)} %\r')
            sys.stdout.flush()
            outfile.write(f"{word},{','.join(list(rhymes))}\n")


parser = argparse.ArgumentParser()
parser.add_argument('--chunk_path', type=str)

args = parser.parse_args()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(args))