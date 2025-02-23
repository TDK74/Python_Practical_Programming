#!/usr/bin/python
# -*- coding: utf-8 -*import

import keyword
keyword.kwlist

import builtins
dir(builtins)

x = 1
x = "test"
print(x)

type(x)

x = "abc"
type(x)

m = [1, 2, 3]
i = iter(m)
i.__next__()
next(i)
next(i)

for i in m:
    print(i)
    
a = b = [5, 4, 3]
a, b

a[1] = 6
a, b

a = b = 1
a = 2
a, b

a = b = [5, 4, 3]
a is b
b is a

a = [5, 4, 3]
b = [5, 5, 3]
a is b
b is a

a = 5; b = 5; c = 5;
import sys
sys.getrefcount(5)

a, b, c, = 5, 4, 3
a, b, c

a, b, c = "abc"
a, b, c

a, b, c = (1, 2, 3)
a, b, c

[a, b, c] = (1, 2, 3)
a, b, c

a, b, c = 1, 2

a, b, *c = 1, 2, 3, 4
a, b, c


a = "1"
type(a)

if type(a) == str:
    print("String")
    
int("String")

bool(1)

int(5.5)

float(5)

str([5, 4, 3])

bytes("String", "utf-8")

bytearray("Hello", "utf-8")

list("Hello")

tuple("Hello")

x = input("Enter x = \n")
y = input("Enter y = \n")
print(x + y)
input()

x = float(input("Enter x = \n"))
y = float(input("Enter y = \n"))
print(x + y)
input()

z = 1
print(z)

del z
print(z)

del a, b, c
