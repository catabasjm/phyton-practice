def add(*args):  # varible name args can be changed
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,))

def hello(**kwargs):  # can also be changed as long as it has **
    print('idk')
    for key,value in kwargs.items():
        print(value, end = ' ')

hello(first = 'jhna', second = "mari", last = 'catabas')

print('the {} jumped over the {}'.format('cow', 'moon'))