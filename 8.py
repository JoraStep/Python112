# Задача №1
import random as r
# w, h = 6, 6
# matrix = [[r.randint(1, 100)for x in range(w)] for y in range(h)]
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()
# print("Минимальный элемент массива: ", min(map(min, matrix)))

w, h = 6, 6
matrix = [[r.randint(1, 10)for x in range(w)] for y in range(h)]
for h in matrix:
    for w in h:
        print(w, end="\t\t")
    print()
a = [r.randint(0, 10) for i in range(6)]
print(a)


























