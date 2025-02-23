#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
# игнорираме регистъра
p = re.compile(r"^[a-z]+$", re.I)
print("Found" if p.search("ABC") else "Not found")
# намерено, макар че в низа символите да са в горен регистър,
# а в шаблона да са от долен

# без игнориране на регистъра на символите
p = re.compile(r"^[a-z]+$")
print("Found" if p.search("ABC") else "Not found")
# не е намерено

p = re.compile(r"^.$")
print("Found" if p.search("\n") else "Not found")

p = re.compile(r"^\a+$")
p = re.compile("^\\a+$") # когато е без "r" отпред

dt = "04.04.2015"
p = re.compile(r"^[0-3][0-9].[01][0-9].[12][09][0-9][0-9]$")
if p.search(dt): print("correct")
    
# точката не съответства на \n
p = re.compile(r"^.+$")
p.findall("s1\ns2\ns3")

# точката съответства на \n
p = re.compile(r"^.+$", re.S)
p.findall("s1\ns2\ns3")

import re

p = re.compile(r"^[0-9]+$", re.S)

num = "123"
snum = "s123"

if p.search(num):
    print("number")
else:
    print("string")

if p.search(snum):
    print("number")
else:
    print("string")

s = "<i>One</i><i>Two</i><i>Three</i>"
p = re.compile(r"<i>.*</i>", re.S)
p.findall(s)

p = re.compile(r"<i>.*?</i>", re.S)
p.findall(s)

p = re.compile('[0-9]+')
print("found" if p.match("s123") else "not found")
print("found" if p.match("123s") else "not found")

p = re.compile('[0-9]+')
print("found" if p.search("s123") else "not found")
print("found" if p.search("123s") else "not found")

# код за проверка на коректен имейл
import re

email = "den@sales.example.com"

pattern = r"^([a-z0-9_.-]+)@(([a-z0-9-]+\.)+[a-z]{2,6})$"
p = re.compile(pattern, re.I | re.S)
m = p.search(email)

if not m:
    print("not match")
else:
    print("match")
#край

p = re.compile(r"[a-z]+")
p.findall("abc, bca, 123, dsf")
p.findall("1234, 12345, 123456")

# използване на метода sub
import re

def mult(m):
    x = int(m.group(0))
    x *= 2
    return "{0}".format(x)

p = re.compile(r"[0-9]+")
# умножаваме всички числа по 2
print(p.sub(mult, "2, 3, 4, 5, 6, 7"))
# умножаваме първите три числа
print(p.sub(mult, "2, 3, 4, 5, 6, 7", 3))
