weight = int(input('Weight: '))
heavy = input('kg or lbs: ')

if heavy == 'kg':
    convert = float(weight) / 0.45
    print('you are ' + str(convert) + ' in lbs')
elif heavy == 'lbs':
    convert = float(weight) * 0.45
    print('you are ' + str(convert) + ' in kg')
else:
    print('pick one of choices')




