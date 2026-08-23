a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
c = int(input('Enter the value of c:'))

import cmath
r = cmath.sqrt(b**2 - 4*a*c)
x_1 = (-b + r)/(2*a)
x_2 = (-b - r)/(2*a)

print(f'The roots of equation are :{x_1}&{x_2}')
