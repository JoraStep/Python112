# Задача №1
# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# c = a
# a = b
# b = c
# print("a:", a)
# print("b:", b)
# Как сделать вторым способом?

# Задача №2
# name = input("What is your name?:")
# age = input("How old are you?:")
# city = input("Where are you live?:")
# print("This is {0}. It is {1} years old. He lives in {2}".format(name, age, city))

# Задача №3

# print("Решите пример : 4 * 100 - 54")
# answer = int(input("Ваш ответ?:"))
# print("Правильный ответ: 346")

# Задача №4
# num = int(input("Введите пятизначное число:"))
# a = num // 10000
# print(a)
# b = (num // 1000) % 10
# print(b)
# c = (num // 100) % 10
# print(c)
# d = (num // 10) % 10
# print(d)
# e = num % 10
# print(e)
# print("Произведение чисел числа : {0} :" .format(num))
# print(a * b * c * d * e)
# print("Среднее арифметическое числа {0}:".format(num))
# print((a + b + c + d + e )/5)


# почему работает не корректно?
# a = int(input("Введите количество ворон: "))
# if a == 1:
#     print(a, "ворона")
# elif 2<=a or a<=4:
#     print(a, "вороны")
# elif a==0 or 4<=a or a<=9:
#     print(a, "ворон")
# else:
#     print("Ошибка ввода данных")

# a, b = 10, 20
# print("делить нельзя" if a == 0 else (b/a))


# a = (input("Введите первое число"))
# b = (input("Введите второе число"))
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
#     b = str(b)
# finally:
#     print(a + b)


# i = 0
# while i < 5:
#     print("i=",i)
#     i+= 1  # i = i +1

# i = 2
# while i < 22:
#     print("i =", i)
#     i += 2

# i = 0
# while i < 22:
#     i += 1
#     if i %2 == 0:
#         print(i)

# n = int(input("Укажите количество символов:"))
# print(n*'*')

# n = int(input("Укажите количество символов:"))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1
# n = int(input("Укажите количество символов:"))
# while n > 0:
#     print("*")
#     n -= 1

# a = int(input('Введите ваше начало диапазона '))
# b = int(input('Введите ваш конец диапазона '))
# s = 0
# while a <=b :
#     if a % 2 != 0:
#        s += a
#     a += 1
# print(s)
# не завершено
# kol = int(input("ВВедите количество чисел последовательности"))
# i = 1
# ch = float(input("Введите число"))
# min_ch = ch
# max_ch = ch
# sum_ch = ch
# while 1 < kol:
#     ch = float(input("Введите число"))
#     if ch < min_ch:
#         min_ch = ch
#     if ch > max_ch = ch
#
#     i += 1
# опять не работает
# n = int(input("Введите целое число:"))
# while type(n) != int:
#     try:
#         n =int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число:")
# if n % 2 == 0:
#      print("Четное")
#  else:
#      print("Нечетное")

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# Задача №2
# a = int(input("Начало диапазона:"))
# b = int(input("Конец диапазона:"))
# for i in range(a, b+1):
#     if(i % 2 != 0):
#         print(i)

# import random # Подключаем модуль random
# print("Игра 'Угадай число'\n")
# # Генерация случайного целого числа от 1 до 100
# n = random.randint (1, 100)
# kol = 0 # Количество шагов
# ch = -1 # Число игрока
# while n != ch:
#     # Ввод числа игрока
#     ch = int(input("Твое число: "))
#     kol += 1
#     # Сравнение задуманного и введенного чисел
#     if n > ch:
#         print("Задуманное число больше\n")
#     elif n < ch:
#         print("Задуманное число меньше\n")
#     else:
#         print("Поздравляю! Ты угадал!")
#         print("Число шагов: ", kol)










# w = int(input("width: "))
# h = int(input("height: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#         print(" ",end="")
#     print()


# a=[int(input('Znachenie')) for i in range(int(input('kolichestvo ')))]
# s=0
# print(a, end=' ')
# print('*-'*20)
# for i in range(len(a)):
#     if a[i]<0:
#         s+=a[i]
# print(s)


# a=list(range(21,41))
# s=0
# d1=0
# print(a)
# print('*-'*20)
# for i in range(len(a)):
#     if a[i]%2==0:
#         s+=1
#     else:
#
#         d1 += a[i]
# print(s)
# print(d1)

# list=[i for i in range(21,41)]
# print(list)
# count=0
# max=0
# for elem in list:
#     if elem%2==0:
#         count+=1
#     if elem%2!=0:
#         max+=elem
# print(count)
# print(max)


# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# s = k = 0
# for i in range(len(a)):
#     if a[i] !=0:
#         s += a[i]
#         k += 1
# print("Среднее арифметическое", s / k)

# #Задача №1
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
#
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#       print(a[i], end=" ")

#Задача №2
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end=" ")


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(a)
# for i in range(len(a)):
#     for b in range(len(a)):
#        if i != b and a[i] == a[b]:
#         break
#     else:
#         print(a[i], end=" ")

# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# s.append(99)
# print(s)
# s.extend([11, 77, 66])
# print(s)

# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# c = []
# for i in range(len(b)):
#     d = b[i]* b[i]
#     c.append(d)
# print(c)


# d = []
# for i in range(1,11):
#     d.extend([i**2])
# print(d)

# d = []
# n=int(input('Введите количество циклов: '))
# for i in range(n):
#     x=int(input('Введите число: '))
#     if x%3==0:
#         d.extend([x])
#     else:
#         print('Пожалуйста, введите число, кратное 3')
# print(d)


# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# print("Введите число для удаления: ")
# k = int(input("k = "))
# a.remove(k)
# print(sorted(a, reverse=True))




import random as r

# city_list =["Moscow", "Novosibirsk", "Voronezh", "Sochi", "Ekaterinburg"]
# print(r.choice(city_list))
#
# s = [55, 66, 77, 88, 99]
# print(r.choice(s))


# s3 = [20, 30, 40, 50, 60, 70, 80, 90]
# print(r.choices(s3,k=3))
#
#
# r.shuffle(s3)
# print(s3)
# print(round(r.uniform(10.5, 25.5),2))

# mas = [i for i in range(10)]
# print(mas)
#
# mas1 = [r.randint(0, 100) for i in range(10)]     #случайное число в заданном диапазоне
# print(mas1)


# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))


# a = [r.randint(0, 100) for i in range(10)]
# print(a)
# b = max(a)
# print(max(a))
# a.remove(b)
# a.insert(0,b)
# print(a)

# a = [r.randint(-10, 10) for i in range(10)]
# print(a)
# a.sort(reverse=True)
# print(a)

# a = [r.randint(0, 100) for i in range(10)]
# print(a)
# b = min(a)  #min
# print(b)
# s = a.index(b)   #index
# print(s)
# del a[0:s]
# print(a)


# x = list("1a2b3")
# print(x)
# print("a" in x)

# lst =[]
# if len(lst) == 0:
#     print("Spisok pust")
#
# if not lst:
#     print("Spisok pust")

# n1 = 5
# n2 = 4
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for j in range(n2)]
# print("Первый список", a)
# print("Второй список", b)
# c = a + b
# print("третий список", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений", c)
# c =[]
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# c =[min(a), min(b), max(a), max(b)]
# print("Минимальное и максимальное для каждого из списков:", c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(m[1][2])
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     for col in row:
#         print(col, end="\t\t")
#     print()

# m = [[1, 2, 3, 4, 7, 9], [5, 6, 7, 8, 2], [9, 10, 11, 12]]
# print(m)
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col]**2, end="\t\t")
#     print()
# print()
#
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# print(a)
# for r in a:
#     for c in r:
#         print(c, end='\t\t')
#     print()
# print()
# for r in a:
#     for c in r:
#         print(c**2, end='\t\t')
#     print()
# print()

# w , h = 5, 4
# matrix = [[r.randint(1, 30)for x in range(w)] for y in range(h)]
# print(matrix)
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()


# w, h = 3, 4
# matrix=[[r.randint(-20,10) for x in range(w)] for y in range(h)]
# c=0
# for row in matrix:
#     for col in row:
#         if col<0:
#             c+=1
#         print(col, end='\t\t')
#     print()
#
# print('количество отрицательных значений: ', c)


# w, h = 6, 6
# matrix=[[r.randint(0, 10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for col in row:
#         print(col, end='\t\t')
#     print()
# print()
# for h in range(len(matrix)):
#     if h % 2 == 0:
#         for w in range(len(matrix[h])):
#             print(matrix[h+1][w], end="\t\t")
#         print()
#         for w in range(len(matrix[h])):
#             print(matrix[h][w], end="\t\t")
#         print()

# 1 2 3 4 5
# 8 9 10 11 12
# 15 16 17 18 19
# 22 23 24 25 26
# 29 30 31
#

# days = [ d for d in range(1, 32)]
# print(days)
# print(len(days))
# weeks = [days[i:i+5]for i in range(0, len(days), 7)]
# print(weeks)
# for row in weeks:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# import math
# print(math.sqrt(2))
# print(math.floor(3.8))
# print(math.ceil(3.2))
#
# c = int(input('Введите радиус окружности'))
#
# print("Радиус окружности равен:", round(2 * math.pi * c))

import time

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# result = finish - start
# print(result)

print(time.strftime("Сегодня: %B %d %Y" , time.localtime()))



















































