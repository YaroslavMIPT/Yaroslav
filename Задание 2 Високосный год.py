year = int(input('Insert year'))

if not year % 4 != 0:
    print('Year is not Leap')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Leap Year')
    else:
        print('Year is not Leap')
else:
    print('Leap Year')
