# pcost.py
#
# Exercise 1.31

import gzip



def portfolio_cost(filename):
        total_cost = 0
        f = open(filename, 'rt')
        headers = next(f).split(',')

        for line in f:
                try:
                        row = line.split(',')
                        total_cost = total_cost + (int(row[1]) * float(row[2]))
                        #print(row)
                except ValueError:
                        print('Data Missing', line)
        f.close()
        return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)