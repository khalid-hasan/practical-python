# report.py
#
# Exercise 2.4

import gzip
import csv
import sys


def read_portfolio(filename):
        portfolio = []
        f = open(filename, 'rt')
        rows= csv.reader(f)
        headers = next(rows)

        for row in rows:
                try:
                        holding = (row[0], int(row[1]), float(row[2]))
                        portfolio.append(holding)
                except ValueError:
                        print('Data Missing', row)
        f.close()
        return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
