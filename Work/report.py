# report.py
#
# Exercise 3.16

import gzip
import csv
import sys
import fileparse


def read_portfolio(filename):

        with open(filename) as lines:
                return fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
        #return fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])

def read_prices(filename):

        with open(filename) as lines:
                return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))
        #return dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))

def make_report(portfolio, prices_dictionary):
    data = []
    for row in portfolio:
        current_price = prices_dictionary[row['name']]
        change = current_price - row['price']
        report = (row['name'], row['shares'], current_price, change)
        data.append(report)
    return data

def portfolio_report(portfolio_filename, prices_filename):
        portfolio = read_portfolio(portfolio_filename)
        print('Total Cost', portfolio)

        prices_dictionary = read_prices(prices_filename)
        print(prices_dictionary)

        report = make_report(portfolio, prices_dictionary)
        headers = ('Name', 'Shares', 'Price', 'Change')
        print('%10s %10s %10s %10s' % headers)
        print(10*'-' + ' ' + 10*'-' + ' ' + 10*'-' + ' ' + 10*'-')
        for name, shares, prices, change in report:
                prices = '$' + str(prices)
                print(f'{name:>10s} {shares:>10d} {prices:>10s} {change:>10.2f}')

def main(argv):
    if len(argv) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % argv[0])
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)