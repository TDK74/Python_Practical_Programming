#!/usr/bin/python
# -*- coding: utf-8 -*-

d = dict()
d = dict(name = 'John', surname = 'Doe'); d
d = dict({"name": "John", "surname": "Doe"}); d
d = dict([["name", "John"], ["surname", "Doe"]]); d
d = dict([("name", "John"), ("surname", "Doe")]); d

keys = ("name", "surname")
values = ("John", "Doe")
list(zip(keys, values))
kv = list(zip(keys, values))
d = dict(kv); d

d = {}
d["name"] = "John"
d["surname"] = "Doe"
d

d = {}
d = {"name": "John", "surname": "Doe"}; d

d2 = d
d2 is d
d2 = d.copy()
d2 is d

import copy
d2 = copy.deepcopy(d); d2
d2 is d

d["name"]
d["lastname"]

"surname" in d
"lastname" in d

len(d2)

d["lastname"] = "Doe"
d

del d["lastname"]; d

for key in d.keys():
    print("({0} => {1})".format(key, d[key]), end = " ")
    
keys = list(d.keys())
keys.sort()
for key in keys:
    print("({0} => {1})".format(key, d[key]), end = " ")
    
d["lastname"] = "Doe"
d["zip"] = "109011"
d

values = d.values()
list(values)

d.get("lastname")
d["lastname"]

d.pop("lastname")
d

s = set()
s

s = set("hello");s
set([1, 2, 3, 4, 5, 4])
set([1, 2, 3, 3, 4, 5])

for i in s: print(i, end = " ")

len(s)

s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
s3 = s1 | s2; s3

s1 |= s2; s1

s1
s2
s1 - s2
s1 -= s2

s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
s1 & s2
s1 ^ s2

s1
3 in s1
4 in s1

s1 == s2

s1
s2
s1 <= s2
s1 >= s2
s1 < s2
s1 > s2

s1
s1.add(4); s1
s1.remove(4); s1
s1.remove(4)
s1.discard(4)

