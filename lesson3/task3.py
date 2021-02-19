
def thesaurus(*args):
    a = {}
    for i in args:
        if i[0] in a:
            a[i[0]].append(i)
        else:
            a[i[0]] = [i]
    return a


print(thesaurus("Ира", "Макс", "Петр", "Илья", "Петров", "Ильич"))
