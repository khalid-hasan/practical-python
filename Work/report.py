# report.py
#
# Exercise 2.4

import gzip
import csv
import sys


def read_portfolio(filename):
        dict_list = []
        total = 0
        f = open(filename, 'rt')
        rows= csv.reader(f)
        headers = next(rows)

        for row in rows:
                try:
                        holding = {
                            'name': row[0], 
                            'shares': int(row[1]), 
                            'prices': float(row[2])
                        }
                        dict_list.append(holding)
                        total += int(row[1]) * float(row[2])
                except ValueError:
                        print('Data Missing', row)
        f.close()
        return [total, dict_list]

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = read_portfolio(filename)
print('Total Cost', cost[0])
print('Dictionary', cost[1])