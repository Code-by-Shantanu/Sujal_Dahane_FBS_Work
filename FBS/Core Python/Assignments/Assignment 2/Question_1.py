hr = int(input('Enter your time in hours:'))
min = int(input('Enter your time in minutes:'))
sec = int(input('Enter your time in seconds:'))

hr = hr*360
min = min*60

total_sec = hr + min + sec

print(f'total_secconds is :{total_sec}')