a = int(input('Enter area of the wall:'))
cost_1 = int(input('Enter cost to paint interier wall:'))
cost_2 = int(input('Enter cost to paint exterior wall:'))

interior_cost = a*cost_1
exterior_cost = a*cost_2

print(f'cost of painting interior is:{interior_cost} and cost of painting exterior is:{exterior_cost}')