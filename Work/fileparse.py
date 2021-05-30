# fileparse.py
#
# Exercise 3.7

import csv

def parse_csv(filename, select=None, types=[str, int, float], has_headers=True, delimiter=','):

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        if(has_headers):
            headers = next(rows)
        else:
            headers = []

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:   
                continue
            if select:
                row = [ row[index] for index in indices ]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError:
                        pass

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

    return records

portfolio = parse_csv('Data/portfolio.dat', types=[str, int, float], has_headers=True, delimiter=' ')
print(portfolio)