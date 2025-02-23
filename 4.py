#!/usr/bin/python
# -*- coding: utf-8 -*import

a = True; b = False; a, b

5 == 5

5 != 6

5 == 6

100 > 99

100 < 99

100 <= 100

100 >= 101

2 in [1, 2, 3]

a = b = 100; a is b

a = b = 100; not (a == 100)

2 not in [1, 5, 7]

a is not b

2 < 5 < 6

2 < 5 and 2 < 6

2 < 5 and 6 < 2

2 < 5 or 2 < 6

2 < 5 or 6 < 2

2 < 1 or 6 < 2

n = int(input("input N: "))
if n < 100:
    print("n < 100")
else:
    print("n > 100")

n = int(input("input N: "));
if n < 100: print("n < 100")
else: print("n > 100")

print(""" Select your browser
1 - Google Chrome
2 - Firefox
3 - MS IExplorer
4 - Opera
5 - Safari
6 - Other """)
browser = int(input(""));
if browser == 1:
    print("Chrome");
elif browser == 2:
    print("Firefox");
elif browser == 3:
    print("MS IE");
elif browser == 4:
    print("Opera");
elif browser == 5:
    print("Safari");
elif browser == 6:
    print("Other");
else:
    print("Incorrect input")

for i in range(1, 10):
    print(i)
else:
    print("Done.")

for i in range(1, 10):
    print(i)
    if i == 6:
        break
else:
    print("Done.")

dict = {"a" : 1, "c" : 3, "b" : 2}
for key in dict.keys():
    print(key, " => ", dict[key])

dict = {"a" : 1, "c" : 3, "b" : 2}
for key in sorted(dict.keys()):
    print(key, " => ", dict[key])

n = 0
while True:
    print("Hello")
    n += 1
    if n == 5: break

n = 0
while n < 10:
    print("Hello again")
    n += 1

for n in range(1, 20):
    if n == 5:
        continue
    if n == 12:
        break
    print(n)

for x in range(1, 100):
    print(x)

for x in range(200, 100, -1):
    print(x)

rng = range(1, 100)
rng.index(5)
rng.count(100)

