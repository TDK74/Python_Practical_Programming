#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

with open ('table.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    
    for row in f_csv:
        # obrabotvane na reda
        # ...
        

from collections import namedtuple

with open ('table.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    
    for r in f_csv:
        row = Row(*r)
        # obrabotvane na reda
        # ...
        
        

import csv

with open ('table.csv') as f:
    f_csv = csv.DictReader(f)
    
    for row in f_csv:
        # obrabotvane na reda
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
        # obrabotvane na reda
        # ...
        
        
import json

data = {
    'firstname' : 'John',
    'lastname' : 'Doe',
    'year' : 1979
}
json_str = json.dumps(data)

data = json.loads(json_str)

# zapisvane na JSON danni
with open('data.json', 'w') as f:
    json.dump(data, f)
    
# prochitane na dannite obratno
with open('data.json', 'r') as f:
    data = json.load(f)
    
    
from urllib.request import urlopen
from xml.etree.ElementTree import parse

# zarejdane na RSS emisiata i parsvane
u = urlopen('http://dkws.org.ua/phpbb2/rss.php')
doc = parse(u)

# izvlichane i izvejdane na tagovete
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    link = item.findtext('link')
    
    print(title)
    print(link)
    print()
    

# nachalen baitov niz
s = b'hello'
# kodirane s 16-en vid
import binascii
h = binascii.b2a_hex(s)
h
#dekodirane v baitove
b = binascii.a2b_hex(h)
b


import base64
h = base64.b16encode(s)
h

b = base64.b16decode(h)
b

print(h.decode('ascii'))

# niakakvi baitovi danni
s = b'hello'
import base64

# kodirane v Base64
a = base64.b64encode(s)
a
# dekodirane ot Base64
b = base64.b64decode(a)
b
