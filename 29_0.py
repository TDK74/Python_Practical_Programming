#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

def hello(n):
    while n > 0:
        print('hello', n)
        n -= 1
        time.sleep(3)
        
# sazdavane i startirane na nishka
from threading import Thread
t = Thread(target = hello, args = (100, ))
t.start()

if t.is_alive():
    print('live')
else:
    print('RIP')
    
t.join()

class HelloThread:
    def __init__(self):
        self._live = True
        
    def terminate(self):
        self._live = False
        
    def start(self, n):
        while self._live and n > 0:
            print('Hello', n)
            n -= 1
            time.sleep(3)

hi = HelloThread()            
t = Thread(target = hi.start, args = (100, ))
t.start()
# ...
hi.terminate()
t.join()



class IOThread:
    def terminate(self):
        self._live = False
        
    def start(self, sock):
        sock.settimeout(5)  # ustanoviavane na taimaut
        while self._live:
            # izpylnenie na blokirashta operacia I/O s taimaut
            try:
                data = sock.recv(4096)
                break
            except socket.timeout:
                continue
            # prodyljavane na rabotata
            #...
        # zavyrsheno
        return
    

t = Thread(target = hello, args = (100, ), daemon = True)
t.start()


from threading import Thread

class HelloThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = 0
        
    def start(self):
        while self.n > 0:
            print('Hello', self.n)
            self.n -= 1
            time.sleep(5)

hi = HelloThread(5)     
hi.start()

import multiprocessing
hi = HelloThread(5)
t = multiprocessing.Process(target = hi.start)
t.start()
# ...



from queue import Queue 
from threading import Thread 

# nishka, koiato proivejda dannite 
def transmitter(out_s):
    while True:
        # izvejdane na dannite
        # ...
        out_s.put(data) 

# nishka, koiato priema dannite
def receiver(in_s):
    while True:
        # poluchavane na dannite
        data = in_s.get()
        
        # obrabotvane na dannite 
        # ...
        
# syzdavane na spodelena opashka i startirane na dvete nishki
q1 = Queue()
t1 = Thread(target = transmitter, args = (q, ))
t2 = Thread(target = receiver, args = (q, ))
t1.start()
t2.start()



from queue import Queue
from threading import Thread 

# obekti, koito syobshtavat za prekratiavane
# (singnalen marker)
_signal = object() 

def transmitter(out_s):
    while running:
        # generirane na niakakvi danni
        # ...
        out _s. put(data) 
        # postaviane na signalnia marker v opashkata - tova 
        # e signal za prekratiavane
        out_s.put(_signal)

# nishkata, koiato potrebiava dannite
def receiver(in_s):
    while True:
        # poluchavane na dannite
        data = in_s.get()
        # proverka za prekratiavane
        if data is _signal:
            in_s.put(_signal)
            break
        # obrabotvane
    # ...
    

from queue import Queue
from threading import Thread
import copy

def transmitter(out_s):
    while running:
        # generirane na danni
        # ...
        out _s. put(copy.deepcopy(data))

def receiver(in_s):
    while True:
        # poluchavane na dannite
        data = in_s.get()
        # obrabotvane na dannite
        # ...

import queue 
q1 = queue.Queue() 

try:
    data = q1.get(block = False)
except queue.Empty:
    # ...

try:
    q1.put(item, block = False)
except queue.Full:
    # ...

try: 
    data = q1.get(timeout = 10.0)
except queue.Empty:
    # ...

def transmitter(q):
    # ...
    try:
        q.put(item, block = False)
    except queue.Full:
        log.warning('item %r', item)

_running = True
def receiver(q):
    while _running:
        try:
            item = q.get(timeout = 10.0)
            # obrabotvane na elementa
            # ...
        except queue.Empty:
            pass
        