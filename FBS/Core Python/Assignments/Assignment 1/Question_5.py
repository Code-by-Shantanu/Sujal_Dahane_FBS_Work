P = int(input('Enter principal amount :'))
T = int(input('Enter no. of years:'))
R = float(input('Enter rate of interest:'))

Compound_Interest = P*(1+R)**T-P

print(f'Compound Interest is :{Compound_Interest}')