names = ['max', 'snow', 'cookie', 'ning', 'neg', 'range']
print(names)
names[0] = 'kobi'
print(names)
print(names[0:3])
names.append('peewee')  # adds last element
print(names)
names.insert(1,'max')
print(names)
names.remove('cookie')
print(names)
names.pop()  # removes last element
names.sort()  # sorts alphabetically

#for i in names:
#    print(i, end=' ')

drinks = ['coke', 'nestea', 'royal']
biscuit = ['bingo', 'presto', 'skyflakes']
bread = ['coco', 'francis', 'sliced']

snacks = [drinks, biscuit, bread]

print(snacks[0][1])


# list comprehension

squares = []
for i in range(1,11):
    squares.append(i * i)
print(squares)

# using list comprehension, less syntax and easier to read
squares = [i * i for i in range(1,11)]
print(squares)


students =[100,90,80,70,60,50,40,30,0]

passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)