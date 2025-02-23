#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

def hello(n):
    while n > 0:
        print('hello', n)
        n -= 1
        time.sleep(3)
        

from threading import Thread
t = Thread(target = hello, args = (100, ))
t.start()

