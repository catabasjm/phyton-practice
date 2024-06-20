# zip()--creates zip obj w paired elements stored in tuples

usernames = ['mjhana', 'janamari', 'jcatabas']
passwords = ['54262', 'jana143', 'jmcat']
log_date = ['1223240', '112424', '100324']


users = zip(usernames, passwords, log_date)

for i in users:
    print(i)