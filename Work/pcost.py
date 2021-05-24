# pcost.py
#
# Exercise 1.32

import gzip
import csv


def portfolio_cost(filename):
        total_cost = 0
        f = open(filename, 'rt')
        rows= csv.reader(f)
        headers = next(rows)

        for row in rows:
                try:
                        total_cost = total_cost + (int(row[1]) * float(row[2]))
                        #print(row)
                except ValueError:
                        print('Data Missing', row)
        f.close()
        return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)