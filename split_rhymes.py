import csv
from pprint import pprint

with open('./test.csv', 'r') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  for row in csvfile:
    print(row)