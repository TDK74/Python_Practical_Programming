#!/usr/bin/python
# -*- coding: utf-8 -*-

# gzip
import gzip
with gzip.open('compressed_file.gz', 'rt') as f:
    text = f.read()

# bz2
import bz2
with bz2.open('compressed_file.bz2', 'rt') as f:
    text = f.read()

# gzip
import gzip
with gzip.open('compressed_file.gz', 'wt') as f:
    f.write(text)

# bz2
import bz2
with bz2.open('compressed_file.bz2', 'wt') as f:
    f.write(text)
    

with open('file.txt', 'rt') as f:
    data = f.read()

with open('bigfile.txt', 'rt') as f:
    for line in f:
        # ...
        

with open('file.txt', 'wt') as f:
    f.write(text1)
    f.write(text2)
    
with open('file.txt', 'rt', encoding = 'utf-8') as f:
    # ...
    
f.close()


with open('file.txt', 'rt', newline = '') as f:
    # ...
    
# coding: utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')  # ?? AttributeError: module 'sys' has no attribute 'setdefaultencoding'

a = 'tekst utf8'
b = u'tekst unicode'
c = a + b

print ('a = ', type(a), a)
print ('b = ', type(b), b)
print ('c = ', type(c), c)

f = open('file.txt', 'rt', encoding = 'ascii')
f.read()


f = open('file.txt', 'rt', encoding = 'ascii', errors = 'replace')
f.read()

g = open('file.txt', 'rt', encoding = 'ascii', errors = 'ignore')
g.read()

with open('somefile.txt', 'rt') as f:
    print('hello world!', file = f)
    
with open('somefile.txt', 'xt') as f:
    f.write('hello\n')


import io
s = io.StringIO()
s.write('hello world\n')

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
path = '/Users/path_to_file/data.csv'

os.path.basename(path)

os.path.dirname(path)

os.path.join('tmp', 'cs', os.path.basename(path))

path = '~/path_to_file/data.csv'
os.path.expanduser(path)

os.path.splitext(path)


import os
names = os.listdir('D:\path_to_file')


import os.path

names = [name for name in os.listdir('D:\path_to_file') if os.path.isfile(os.path.join('D:\path_to_file', name))]


dirnames = [name for name in os.listdir('D:\path_to_file') if os.path.isdir(os.path.join('D:\path_to_file', name))]

txtfiles = [name for name in os.listdir('D:\\path_to_file') if name.endswith('.txt')]



import os
fd = os.open('file.txt', os,O_WRONLY | os.O_CREAT)


f = open(fd, 'wt')
f.write('hello world\n')
f.close()


f = open(fd, 'wt', closed = False)
# ...


from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:

    f.write('Hello\n')
    f.write('Example\n')
    

    f.seek(0)
    data = f.read()
    

    
with TemporaryFile('w+t', encoding = 'utf-8', errors = 'ignore') as f:
# ? TypeError: NamedTemporaryFile() got an unexpected keyword argument 'errors'


from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('temp file name:', f.name)

    
with NamedTemporaryFile('w+t', delete = False) as f:
    print('temp file name:', f.name)
    

from tempfile import TemporaryDirectory

with TemporaryDirectory() as dirname:
    print('tempdir:'. dirname)
    # ...
    
