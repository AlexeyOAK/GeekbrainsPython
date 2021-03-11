a = []
with open('db_bda.txt') as f:
    for line in f:
        b = line.split()
        a.append((b[0], b[5].replace('"', ''), b[6]))

print(a)