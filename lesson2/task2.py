a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


for i, val in enumerate(a):
    if val.isdigit():
        if len(val) == 1:
            a[i] = '0'+a[i]
    else:
        if val[1:].isdigit():
            if len(val[1:]) == 1:
                a[i] = val[0:1]+'0' + val[1:]


a[1:2] = ['"', a[1], '"']
a[5:6] = ['"', a[5], '"']
a[-2:-1] = ['"', a[-2], '"']

print(a)

