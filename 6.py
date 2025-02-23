#!/usr/bin/python
# -*- coding: utf-8 -*-

str = "hello"
str[1]
str[1] = "r"

s = "привет"
s.encode(encoding = "utf-8")
s.encode(encoding = "cp1251")

s = bytes("hello", "utf-8")
s[0], s[1], s[2]
s

len("Асеневци")
len(bytes("Асеневци", "utf-8"))

s = bytearray("hello", "utf-8")
s[0] = 50; s

a = "hello"; a
b = 'hi'; b

s = "hello\\nworld"; s

s = '''hello,
****
world! ****'''

s = str(b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82', 'utf-8'); s

def func1():
    """ This is documentation string """
    pass

print(func1,_doc_)
print(func1, __doc__)

print(r"c:\test\test.py")

print("c:\\test\\test.py")

s = "123"
s[0], s[1], s[2]
s[3]
s[-1], s[-2], s[-3]

s = "hello"
s[:]
s[:-1:]
s[1::2]
s[1::]

print("1" + "2")
print("1" "2")

s = "1", "2"
type(s)

print("3", s)

"hell" in "Hello"
"hell" in "hello"

print("*" * 20)

len("123456")

s = "123456"
for i in range(len(s)): print(s[i], end = " ")

"%s/%s/%s" % (30, 10, 2010)

"%(car)s - %(year)s" % {"car" : "bmw", "year" : 1978}

"%#x %#x" % (0xfff, 100)

"%+d %+d" % (-3, 3)

"'%10d' - '%-10d'" % (5, 5)

from math import *
"%s %f %.2f" % (e, e, e)

template = """<html>
<head>
    <title>%(title)s</title>
<head>
<body>
%(text)s
</body>
<html>"""

data = {"title": "My site",
       "text": "Content"}

print(template % data)

s = "hello"
s.center(20)
s.center(20, '*')
s.ljust(20)
s.rjust(20)

"{0}/{1}/{2}".format(30, 10, 2010)

"{0}/{1/{2}}".format(*arr)

"{firstname} {lastname}".format(firstname = "John", lastname = "Doe")

"{lastname}, {0}".format("John", lastname = "Doe")

"'{0:<15}' '{1:>15}'".format('hello', 'hello')

"'{0:*<15}' '{1:&>15}'".format('hello', 'hello')

"'{0:G}' '{1:e}'".format(pi, pi)

str("Hello")

repr("hello")

ascii("hello")

ascii("Асеневци")

len("Асеневци")

s = " hello \n"
s.strip()
s
s.lstrip()
s.rstrip()


s = "field1 field2 field3"
s.split()
s.split(None, 1)


s.partition(" ")
s.rpartition(" ")


sep = " "
s1 = sep.join(["field1", "field2"])
s1


s = "hello, world"
s.capitalize()
s.title()
s.upper()
s.lower()
s.swapcase()

chr(55)
ord('7')
chr(5055)

import locale
locale.setlocale(locale.LC_ALL, ('bulgarian'))

s = "hello, world"
num = s.find("world")
num

s.startswith('world')
s.endswith("world")

s.replace('world', 'reader!')

age = input('enter your age: ')
if age.isdigit() == True:
    print('Ok')
else:
    print('error')

import hashlib
hash = hashlib.md5(b"secret")
hash.digest()
hash.hexdigest()
