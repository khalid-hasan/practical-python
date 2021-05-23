# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment = 1000
extra_payment_duration = 12
extra_payment_start_month  = 61
extra_payment_end_month = 108

while principal > 0:
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    months = months + 1

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print(f'{months} {total_paid:0.2f} {principal:0.2f}')
    #Exercise 1.10 has already been implemented in the previous commit.

print('Total paid', total_paid)
print('Total months', months)