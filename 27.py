#!/usr/bin/python
# -*- coding: utf-8 -*-

# kompresia gzip
import gzip
with gzip.open('compressed_file.gz', 'rt') as f:
    text = f.read()

# kompresia bz2
import bz2
with bz2.open('compressed_file.bz2', 'rt') as f:
    text = f.read()

# kompresia gzip
import gzip
with gzip.open('compressed_file.gz', 'wt') as f:
    f.write(text)

# kompresia bz2
import bz2
with bz2.open('compressed_file.bz2', 'wt') as f:
    f.write(text)
    
# prochitane na celia fail v edin niz
with open('file.txt', 'rt') as f:
    data = f.read()
# obhojdane na prochetenite redove ot faila
with open('bigfile.txt', 'rt') as f:
    for line in f:
        # obrabotvane na niza
        # ...
        
# zapisvane na fragmenti ot tekstovi danni
with open('file.txt', 'wt') as f:
    f.write(text1)
    f.write(text2)
    
with open('file.txt', 'rt', encoding = 'utf-8') as f:
    # ...
    
f.close()

# prochitane na fail s izkliucheno preobrazuvane na simvola za nov red
with open('file.txt', 'rt', newline = '') as f:
    # ...
    
# coding: utf8
# ustanoviavane na standartna vanshna kodirovka = utf8
import sys
reload(sys)                     # ??
sys.setdefaultencoding('utf8')  # ?? AttributeError: module 'sys' has no attribute 'setdefaultencoding'

a = 'tekst utf8'
b = u'tekst unicode'
c = a + b

print ('a = ', type(a), a)
print ('b = ', type(b), b)
print ('c = ', type(c), c)

f = open('file.txt', 'rt', encoding = 'ascii')
f.read()

# zameniane na nepravilnite Unicode simvoli s U+fffd
f = open('file.txt', 'rt', encoding = 'ascii', errors = 'replace')
f.read()
# izcialo ignorirane na "loshite" simvoli
g = open('file.txt', 'rt', encoding = 'ascii', errors = 'ignore')
g.read()

with open('somefile.txt', 'rt') as f:
    print('hello world!', file = f)
    
with open('somefile.txt', 'xt') as f:
    f.write('hello\n')


import io
s = io.StringIO()
s.write('hello world\n')
# failov interfeis okolo niz
s = io.StringIO('hello\nworld\n')
s.read(4)
s.read()


import os
import mmap

def memory_map(filename, access = mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    
    return mmap.mmap(fd, size, access = access)

map = memory_map('file.dat')
len(map)

map[0:12] = "Hello, world"
map.close

with memory_map('file.dat') as map:
    print(len(map))
    print(map[0:12])
    # ...
map.closed

map = memory_map(file, mmap.ACCESS_COPY)


import os
path = '/Users/Admin/Documents/Corsair_Link_20180730_08_46_31.csv'
# poluchavane na poslednia komponent na patia
os.path.basename(path)
# poluchavane na imeto na papkata
os.path.dirname(path)
# obediniavane zaedno na komponentite na patia
os.path.join('tmp', 'cs', os.path.basename(path))
# razshiriavane na domashnata papka na potrebitelia
path = '~/Documents/data.csv'
os.path.expanduser(path)
# otdeliane na razshirenieto na faila
os.path.splitext(path)


import os
names = os.listdir('J:\soft_Humblebundle')


import os.path
# poluchavane na vsichki obiknoveni failove
names = [name for name in os.listdir('J:\LTspice_simulations') if os.path.isfile(os.path.join('J:\LTspice_simulations', name))]

# poluchavane na vsichki papki
dirnames = [name for name in os.listdir('J:\LTspice_simulations') if os.path.isdir(os.path.join('J:\LTspice_simulations', name))]

txtfiles = [name for name in os.listdir('J:\\rabota') if name.endswith('.txt')] # \\ zaradi malkoto r. Ako e goliamo R, stava s edin \


# otvariane na deskriptor na faila ot nisko nivo
import os
fd = os.open('file.txt', os,O_WRONLY | os.O_CREAT)

# prevrachtane v obiknoven failov obekt
f = open(fd, 'wt')
f.write('hello world\n')
f.close()

# sazdavane na failov obekt, no fd ne tribva da se zatvaria
# sled zatvarianeto na f
f = open(fd, 'wt', closed = False)
# ...


from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # chetene/zapis vyv faila
    f.write('Hello\n')
    f.write('Example\n')
    
    # prevyrtane v nacjaloto i chetene na dannite
    f.seek(0)
    data = f.read()
    
    # vremennia fail e unishtojen
    
with TemporaryFile('w+t', encoding = 'utf-8', errors = 'ignore') as f:
# ? TypeError: NamedTemporaryFile() got an unexpected keyword argument 'errors'


from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('temp file name:', f.name)
    
    # failat shte bade unishtojen avtomatichno
    
with NamedTemporaryFile('w+t', delete = False) as f:
    print('temp file name:', f.name)
    

from tempfile import TemporaryDirectory

with TemporaryDirectory() as dirname:
    print('tempdir:'. dirname)
    # izpolzvane na papka
    # ...
    # papkata i cialoto sadarjanie shte bade iztrito
    
