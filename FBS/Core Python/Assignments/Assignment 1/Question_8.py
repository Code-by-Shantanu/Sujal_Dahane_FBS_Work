days = int(input('Enter days:'))

years = days // 365
weeks = (days%365) // 7
days =  weeks%7

print(f'{years}years:{weeks}weeks:{days}days')