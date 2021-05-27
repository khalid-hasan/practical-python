# report.py
#
# Exercise 2.11

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
                holding = {
                        'name': row[0], 
                        'shares': int(row[1]), 
                        'prices': float(row[2])
                }
                dict_list.append(holding)
                total += int(row[1]) * float(row[2])

        f.close()
        return [total, dict_list]

def read_prices(filename):
        dictionary = {}
        f = open(filename, 'rt')
        rows= csv.reader(f)

        for row in rows:
                try:
                        dictionary[row[0]] = float(row[1])
                        
                except IndexError:
                        pass
        f.close()
        return dictionary

def make_report(portfolio, prices_dictionary):
    data = []
    for row in portfolio:
        current_price = prices_dictionary[row['name']]
        change = current_price - row['prices']
        report = (row['name'], row['shares'], current_price, change)
        data.append(report)
    return data

portfolio = read_portfolio('Data/portfolio.csv')
print('Total Cost', portfolio[0])
print('Dictionary', portfolio[1])

prices_dictionary = read_prices('Data/prices.csv')
print(prices_dictionary)

report = make_report(portfolio[1], prices_dictionary)
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(10*'-' + ' ' + 10*'-' + ' ' + 10*'-' + ' ' + 10*'-')
for name, shares, prices, change in report:
        prices = '$' + str(prices)
        print(f'{name:>10s} {shares:>10d} {prices:>10s} {change:>10.2f}')