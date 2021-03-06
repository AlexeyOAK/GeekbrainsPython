# при любых значениях выводит любую длину без ошибок
gena = (num for num in range(1, int(input()) + 1, 2))
print(*gena)