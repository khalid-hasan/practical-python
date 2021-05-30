# pcost.py
#
# Exercise 1.33

import gzip
import csv
import sys
import report

def portfolio_cost(filename):
        total_cost = 0
        portfolio = report.read_portfolio(filename)
        for rows in portfolio:
                nshares = int(rows['shares'])
                price = float(rows['price'])
                total_cost += nshares * price
        return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)