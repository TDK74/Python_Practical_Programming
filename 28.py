#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

with open ('table.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    
    for row in f_csv:
        # ...
        

from collections import namedtuple

with open ('table.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    
    for r in f_csv:
        row = Row(*r)
        # ...
        
        

import csv

with open ('table.csv') as f:
    f_csv = csv.DictReader(f)
    
    for row in f_csv:
        # ...
        
        
headers = ['UserID', 'FirstName', 'LastName']
rows = [('user1', 'John', 'Doe'), ('user2', 'Jane', 'Doe')]

with open('users.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerow(rows)
    # ...
    
    
with open ('users.csv') as f:
    f_tsv = csv.reader(f, delimeter = '\t')
        
    for row in f_tsv:
        # ...
        
        
import json

data = {
    'firstname' : 'John',
    'lastname' : 'Doe',
    'year' : 1979
}
json_str = json.dumps(data)

data = json.loads(json_str)


with open('data.json', 'w') as f:
    json.dump(data, f)
    

with open('data.json', 'r') as f:
    data = json.load(f)
    
    
from urllib.request import urlopen
from xml.etree.ElementTree import parse


u = urlopen('http://dkws.org.ua/phpbb2/rss.php')
doc = parse(u)


for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    link = item.findtext('link')
    
    print(title)
    print(link)
    print()
    


s = b'hello'

import binascii
h = binascii.b2a_hex(s)
h

b = binascii.a2b_hex(h)
b


import base64
h = base64.b16encode(s)
h

b = base64.b16decode(h)
b

print(h.decode('ascii'))


s = b'hello'
import base64


a = base64.b64encode(s)
a

b = base64.b64decode(a)
b
