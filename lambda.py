#  lambda function

# def double(x):
#     return x * 2

# print(double(6))

double = lambda x: x * 2

print(double(6))

multiply = lambda x, y: x * y
print(multiply(3, 5))

full_name = lambda first_name, last_name: first_name+ " "+last_name
print(full_name('Jhana', 'Catabas'))

age_check = lambda age: True if age >= 18 else False
print(age_check(18))