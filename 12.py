#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
time.time()

t = time.time()
time.gmtime(t)

tm = time.gmtime(t)
tm.tm_hour

time.localtime()

time.strftime("%d.%m.%y")
time.strftime("%d.%m.%Y")
time.strftime("%H:%M:%S")

import locale
locale.getlocale()
locale.setlocale(locale.LC_ALL, ('bulgarian'))
print(time.strftime("%A %d %b %Y %H:%M:%S \n%d.%m.%Y"))

import calendar
c = calendar.LocaleTextCalendar(0, "Bulgarian_Bulgaria.1251")
print(c.formatyear(2018))

import time as t
t.sleep(10)

import timeit
t = timeit.Timer('char in text', setup = 'text = "sample string"; char = "g"')
t.timeit()
t.repeat()

from time import *
t1 = time()

print('Hello')
t2 = time()
t = t2 - t1
