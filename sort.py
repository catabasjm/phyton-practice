students = ['Jhana', 'Marie', 'Felix', 'Recamel', 'Jovan', 'Jamaica', 'Zhane', 'Lorane']

# sort method works only in Lists
students.sort()  #  sorts alphabetically
students.sort(reverse=True)

for i in students:
    print(i)

#  sorted() function used in iterables

students = ('jhana', 'marie', 'ayana') #  this is a tuple
sorted_students = sorted(students)
sorted_students = sorted(students, reverse=True)
for i in sorted_students:
    print(i)

#  list of tuples

students = [('Jhana', 'f', 20),
            ('Marie', 'f', 24),
            ('Joban', 'm', 21),
            ('Recamel', 'f', 20)]

ages = lambda age:age[2]
students.sort(key=ages)
students.sort(key=ages, reverse=True)

for i in students:
    print(i)