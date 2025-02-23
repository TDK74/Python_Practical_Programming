#!/usr/bin/python
# -*- coding: utf-8 -*-

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
