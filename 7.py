#Задача №1
# import random as r
# a = [r.randint(0, 100) for i in range(20)]
# print(a)
# print("Сумма: ", sum(a))

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(a)
for r in a:
    for c in r:
        print(c, end='\t')
    print()
print()
