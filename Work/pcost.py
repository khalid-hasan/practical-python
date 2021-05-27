# pcost.py
#
# Exercise 1.33

import gzip
import csv
import sys


def portfolio_cost(filename):
        total_cost = 0
        f = open(filename, 'rt')
        rows= csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
                try:
                        total_cost = total_cost + (int(row[1]) * float(row[2]))
                        #print(row)
                except ValueError:
                        print(f'Row {rowno}: Couldn\'t convert: {row}')
        f.close()
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)