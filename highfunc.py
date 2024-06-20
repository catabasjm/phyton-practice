#  higher order function
#  1. accepts func as argument

def loud(txt):
    return txt.upper()
def quiet(txt):
    return txt.lower()

def hello(func):   #  this is a higher order func accepts as argument
    txt = func('jhAnA')
    print(txt)

hello(loud)
hello(quiet)

#  2. returns func
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))

