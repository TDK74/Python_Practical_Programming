#!/usr/bin/python
# -*- coding: utf-8 -*-

tup = (1, 2, 3, 4)
tup[2]
tup[2] = 5

tup = ()
tup = (1, )
tup = (1, 2, 3)
tup = (1, "str", 3)

tup = tuple()
tup = tuple('hello')
tup = tuple([1, 2, 3])

tup = 1, 2, 3, 4
tup

tup = (1, 2, 3, 4, 5)
tup[4]
tup[::-1]
tup[2:3]
tup[1:3]
7 in tup
2 in tup
tup * 2
tup + (1, 2, 4)

tup = (1, 2, 3, 4, 5, 2, 7)
tup.index(2)
tup.index(2, 2)
tup.count(2)

import itertools as it
for i in it.count():
    if i > 15: break
    print(i, end = " ")
    
list(it.repeat('*', 10))    # списък от '*'
list(zip(it.repeat(3), 'abc'))    # комбинация от функциите zip() и repeat()
list(it.combinations('abc', 2))
list(it.combinations_with_replacement([1, 2, 3], 2))
list(it.permutations('abc', 2))
list(it.dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))

it.tee([1, 2, 3, 4], 2)
