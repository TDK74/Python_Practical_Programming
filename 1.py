#!/usr/bin/python
# -*- coding: utf-8 -*import

# this is comment
print('Hi') # another comment

print('# comment')

# more than one line
# comment

"""
multilines
comment
"""

a = 1; b = 2;
print(a, b)
print(a, b, sep = '\t')

print()

import sys;
sys.stdout.write("hello")
sys.stdout.write("hello\n")

name = input("what is your name? ")
print("hello, ", name)

name = input("what is your name?\n")

try:
  name = input("what is your name? ")
  print(name)
except EOFError:
  print("EOFError raised")
  
import sys
args = sys.argv[:]
for n in args:
  print(n)
