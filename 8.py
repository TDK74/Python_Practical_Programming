#!/usr/bin/python
# -*- coding: utf-8 -*-

lst = [1, 2, 3, 4]
lst[1]
lst[1] = 7
lst

lst = list('hello')
lst

lst = ["a", "b", 1]
lst

lst = []
lst.append(1)
lst.append(2)
lst.append(3); lst

a = b = ["a", "b"]
a[0]
b[0] = 1
a[0]

a is b

lst = []
for i in range(3): lst.append([])
lst[0].append(1)
lst

lst = [1, 2, 3]
lst[1] = 6

a, b, *c = [1, 2, 3, 4]

lst[4]

lst = [1, 2, 3, 4, 5, 6, 7]
lst[-2]

# в обратен ред
lst[::-1]
# без последния елемент
lst[:-1]
# без първия елемент
lst[1:]
# първите три
lst[0:3]
# последния елемент
lst[-1:]

lst[1:3] = [8, 9]
lst

lst2 = [10, 11, 12]
lst3 = lst + lst2; lst3

lst += [10, 11, 13]; lst

lst = [[1, 2, 3], ['a', 'b', 'c'], [9, 8, 7]]
lst
lst[1][2]

# обхождане на всички елементи в списък
for i in lst: print(i, end = " ")

lst = [1, 2, 3, 4]
for i in range(len(lst)): print(lst[i], end = " ")

lst = [[1, 2, 3], ['a', 'b', 'c'], [9, 8, 7]]
2 in lst

lst = [1, 2, 3, 4]
2 in lst

lst.index(3)
lst.index(7)

lst = [1, 2, 2, 3, 4]
lst.count(2)
lst.count(3)
lst.count(7)

min(lst); max(lst)

lst = [1, 2, 3, 4]
lst.append(5)
lst

lst += [6, 7]
lst

# поставяне на 0 в началото на списъка
lst.insert(0, 0)
lst
# поставяне на 8 на позиция 8
lst.insert(8, 8)
lst

lst.pop(0)
lst

lst.pop()
lst

del lst[6]
lst

lst.remove(5)
lst

import random
lst = [1, 2, 2, 3, 4]
random.shuffle(lst)
lst

random.choice(lst)
random.choice(lst)

lst
lst.reverse()
lst

lst = [2, 3, 7, 5, 6, 1, 4]
lst.sort()
lst

lst.sort(reverse = True)
lst

# подреждане на елементите спрямо регистъра на символите
lst.sort(key = str.lower)

lst = ['h', 'e', 'l', 'l', 'o']
s = "".join(lst)
s

# списъци в Python
a = [2, 2, 2, 2]
b = [3, 3, 3, 3]
a * 2
a + 10
a + b

# масиви в NumPy
import numpy as np
an = np.array([2, 2, 3, 3])
bn = np.array([5, 5, 7, 7])
an * 2
an + 10
an + bn
an * bn
np.sqrt(an)
np.cos(an)

grid = np.zeros(shape = (10000, 10000), dtype = float)
grid
grid += 100
grid

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a
# ред 0
a[1]
# колонка 1
a[:, 1]
# избор на фрагмент от масива и промяна
a[1:3, 1:3]
a[1:3, 1:3] += 10
a
