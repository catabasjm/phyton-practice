#  filter(function, iterable)
friends = [('jhana', 20),
           ('mari', 19),
           ('aya', 18),
           ('rei', 17)]

age = lambda data:data[1] >= 18

alcohol_buddy = list(filter(age, friends))

for i in alcohol_buddy:
    print(i)