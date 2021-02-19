a = [23.5, 24.34, 23, 76.1, 34.12, 31, 21.1, 45.45, 33]
a2 = a
for i, x in enumerate(a):
    a[i] = str(x).split('.')
    a[i][0] = a[i][0] + ' руб'
    if len(a[i]) > 1:
        if len(a[i][1]) == 1:
            a[i][1] = '0' + a[i][1]
        a[i][1] = a[i][1] + ' коп'
    else:
        a[i].append('00 коп')
    a[i] = ' '.join(a[i])
print( ', '.join(a))
a.sort()
print(a)
if id(a) == id(a2):
    print(id(a), 'and', id(a2), 'Они явно равны, сравните сами)))')

b = []
for i in a:
    b.append(i)
b.sort(reverse=-1)
print(b)
var = sorted(b)[-5:]
print(var)
