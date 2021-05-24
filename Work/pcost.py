# pcost.py
#
# Exercise 1.27

import gzip

total_cost = 0

f = gzip.open('Data/portfolio.csv.gz', 'rt')
headers = next(f).split(',')

for line in f:
        row = line.split(',')
        total_cost = total_cost + (int(row[1]) * float(row[2]))
        print(row)
print('Total cost', total_cost)
f.close()