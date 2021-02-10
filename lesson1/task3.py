a = list(range(21))

for i in a:
    if 1 < i < 5:
        print(i, 'процента')
    elif 5 <= i <= 20 or i == 0:
        print(i, 'процентов')
    else:
        print(i, 'процент')