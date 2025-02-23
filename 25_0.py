#!/usr/bin/python
# -*- coding: utf-8 -*-

fname = 'report.txt'
fname.endswith('.txt')
fname.startswith('file://')
url = 'http://www.dkws.org.ua'
url.startswith('http://')

fname = 'report.txt'
fname[-4:] == '.txt'
url = 'http://www.dkws.org.ua'
url[:5] == 'http://' or url[:6] == 'https://' or url[:4] == 'ftp:' 

import re
url = 'http://www.dkws.org.ua'
re.match('http: | https: | ftp:', url)

if any(name.endswith('.py', '.pyw') for name in listdir(dirname)):
    # ...

s = 'field1 field2; field3, field4,field5, field6'

import re
re.split(r'[;,\s]\s*', s)

from fnmatch import fnmatch, fnmatchcase
fnmatch('report.txt', '*.txt')
fnmatch('report10.txt', 'report*.txt')
fnmatch('Doc45.xls', 'Doc[0-9]*')
names = ['Doc1.xls', 'Doc2.xls', 'report.txt', 'for.py']
[name for name in names if fnmatch(name, 'Doc*.xls')]

# Windows
fnmatch('report.txt', '*.TXT')
# Linux / FreeBSD / UNIX
fnmatch('report.txt', '*.TXT')

fnmatchcase('report.txt', '*.TXT')

text = 'Lorem ipsum dolor sit amet.'
text.replace('Lorem', 'Ipsim')

text = '03/03/2015.'

import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)

text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags = re.IGNORECASE)

import re
num = re.compile('\d+')

num.match('123456')

num.match('\u0661\u0662\u0663')

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

p = re.compile('hell\u00dfe', re.IGNORECASE)
s = 'hello'
p.match(s)
p.match(s.upper())
s.upper()

import unicodedata
s = unicodedata.normalize('NFD', s)


s = ' hello world \n '
s.strip()
s = ' hello world \n '
s.lstrip()
s = ' hello world \n '
s.rstrip()


t = '-----hello====='
t.lstrip('-')
t.strip('-=')

str = "Hello"
str.ljust(15)
str.rjust(15)
str.center(15)

str.rjust(15, '+')
str.center(15, '*')

format(str, '>20')
format(str, '<20')
format(str, '^20')
format(str, '+>20s')
format(str, '*^20s')

'{:>10s} {:>10s}'.format('hello', 'world')

x = 2.2345
format(x, '>10')
format(x, '^10.2f')

s = "Lorem lpsum dolor sit amet, consectetur adipiscing ellt. Curabltur tempor nunc a porttitor convallis. \
    Vivamus eget dui purus. Nam feugiat ex non eros viverra posuere."

import textwrap
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent = ' '))
print(textwrap.fill(s, 40, subsequent_indent = ' '))

text = 'var = 5 + 5 * 5'
tokens = [('NAME', 'var'), ('EQ', '='), ('NUM', '5'), ('PLUS', '+'), ('NUM', '6'), ('TIMES', '*'), ('NUM', '5')]

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)' 
TIMES = r'(?P<TIMES>\*)' 
EQ = r'(?P<EQ>=)' 
WS = r'(?P<WS>\s+)' 

main_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scan = main_pat.scanner('var = 5')
scan.match()
_.lastgroup, _.group()
scan.match()
_.lastgroup, _.group()
scan.match()
_.lastgroup, _.group()
scan.match()
_.lastgroup, _.group()
scan.match()
_.lastgroup, _.group()
scan.match()

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)' 
TIMES = r'(?P<TIMES>\*)' 
EQ = r'(?P<EQ>=)' 
WS = r'(?P<WS>\s+)' 

main_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

from collections import namedtuple 

Token = namedtuple('Token', ['type', 'value']) 

def generate_tokens(p, text): 
    scan = p.scanner(text)
    
    for s in iter(scan.match, None):
        yield Token(s.lastgroup, s.group()) 

for tokens in generate_tokens(main_pat, 'var = 5 + 7 * 2'):
    print(tokens)
