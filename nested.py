row = int(input('enter num of rows: '))
clms = int(input('enter num of columns: '))
sym = input('enter a symbol: ')

for i in range(row):
    for j in range(clms):
        print(sym, end = "")
    print()