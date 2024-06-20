first_num = int(input('enter first num: '))
second_num = int(input('enter 2nd num: '))

operate = input('+, -, * , /: ')

if operate == '+':
    sum = first_num + second_num
    print(sum)
elif operate == '-':
    diff = first_num - second_num
    print(diff)
elif operate == '*':
    prod = first_num * second_num
    print(prod)
elif operate == '/':
    quot = first_num / second_num
    print(quot)
else:
    print('enter one of choices')

