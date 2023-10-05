print('Введите элементы первого списка:')
a = input().split()
print('Введите элементы второго списка:')
b = input().split()

A = set(a)
B = set(b)

print('\n')

print('Уникальные элементы первого списка:')
print(A)
print('Уникальные элементы второго списка:')
print(B)

C = A.union(B)
print('Уникальные элементы для объединения 1 и 2:')
print(C)

D = A.intersection(B)
print('Элементы, встречающиеся в обоих списках:')
print(D)
