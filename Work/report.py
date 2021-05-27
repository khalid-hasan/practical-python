# report.py
#
# Exercise 2.6

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

cost = read_portfolio('Data/portfolio.csv')
print('Total Cost', cost[0])
print('Dictionary', cost[1])

dict_list = read_prices('Data/prices.csv')
print(dict_list)