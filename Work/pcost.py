# pcost.py
#
# Exercise 3.16

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

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile')
    cost = portfolio_cost(argv[1])
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)

