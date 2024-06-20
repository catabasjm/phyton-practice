def hello(first, last, old):  # set parameters to use
    print('watchu doing')
    print('my name is: ' + last, first)
    print('i am ' +str(old)+ ' yrs old')


name = 'jhana'
my_name = 'catabas'
age = 20

hello(name, my_name, age)  # arguments inside

def sum(num1, num2):
    result = num1 + num2
    return result

print(sum(5,5))

def multiply(num1, num2):
    result = num1 * num2
    return result

x = multiply(7, 8)
print(x)

def subtract(num1, num2):
    return num1 - num2

x = subtract(7,9)
print(x)
