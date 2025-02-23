#!/usr/bin/python
# -*- coding: utf-8 -*-

def msum(x, y):
    return x + y
k = msum(3, 5)
print(k)

s = msum
k = s(3, 5)

def msum(x, y):
    return x + y
def fsum(f, x, y):
    return f(x, y)
k = fsum(msum, 3, 5)

def msum(x, y = 1):
    return x + y
k = msum(3)
msum(y = 3, x = 2)

l1 = (2, 3)
msum(*l1)

d = {"x": 5, "y": 6}
msum(**d)

def test(x):
    x = 1
    return x
y = 2
test(y)

def psum(*k):
    result = 0
    for i in k:
        result += i
    return result
k = psum(1, 2, 3, 4)
print (k)

f1 = lambda: 2 + 2
print(f1())
f2 = lambda x, y: x + y
print(f2(2, 2))

def gen(x, y):
    for i in range (1, x + 1):
        yield i + y
s = gen(3, 3)
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())

def deco(f):
    print("my_func is running")
    return f
@deco
def my_func(x):
    return x * 2
print(my_func(5))

def fact(n):
    if n == 0 or n == 1: return 1
    else:
        return n * fact(n-1)
fact(5)    

glob_var = 5
def func():
    print(glob_var)
    glob_var = 10
func()

def func():
    global glob_var
    glob_var = 10
glob_var = 5
func()
print(glob_var)
